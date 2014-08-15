#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexandre Pinto'
__version__ = "1.0"

from PIL import Image
import random,sys,argparse

def scramble_blocks(im,granularity,password,nshuffle):
	set_seed(password)
	width=im.size[0]
	height=im.size[1]

	block_width=find_block_dim(granularity,width)		#find the possible block dimensions
	block_height=find_block_dim(granularity,height)

	grid_width_dim=width/block_width				#dimension of the grid
	grid_height_dim=height/block_height

	nblocks=grid_width_dim*grid_height_dim			#number of blocks

	print "nblocks: ",nblocks," block width: ",block_width," block height: ",block_height
	print "image width: ",width," image height: ",height
	print "getting all the blocks ..."
	blocks=[]
	for n in xrange(nblocks): #get all the image blocks
		blocks+=[get_block(im,n,block_width,block_height)]

	print "shuffling ..."
	#shuffle the order of the blocks
	new_order=range(nblocks)
	for n in xrange(nshuffle):
		random.shuffle(new_order)

	print "building final image ..."
	new_image=im.copy()
	for n in xrange(nblocks):
		#define the target box where to paste the new block
		i=(n%grid_width_dim)*block_width				#i,j -> upper left point of the target image
		j=(n/grid_width_dim)*block_height
		box = (i,j,i+block_width,j+block_height)	

		#paste it	
		new_image.paste(blocks[new_order[n]],box)

	return new_image



#find the dimension(height or width) according to the desired granularity (a lower granularity small blocks)
def find_block_dim(granularity,dim):
	assert(granularity>0)
	candidate=0
	block_dim=1
	counter=0
	while counter!=granularity:			#while we dont achive the desired granularity
		candidate+=1
		while((dim%candidate)!=0):		
			candidate+=1
			if candidate>dim:
				counter=granularity-1
				break
		
		if candidate<=dim:
			block_dim=candidate			#save the current feasible lenght

		counter+=1

	assert(dim%block_dim==0 and block_dim<=dim)
	return block_dim

def unscramble_blocks(im,granularity,password,nshuffle):
	set_seed(password)
	width=im.size[0]
	height=im.size[1]

	block_width=find_block_dim(granularity,width)		#find the possible block dimensions
	block_height=find_block_dim(granularity,height)

	grid_width_dim=width/block_width				#dimension of the grid
	grid_height_dim=height/block_height

	nblocks=grid_width_dim*grid_height_dim			#number of blocks

	print "nblocks: ",nblocks," block width: ",block_width," block height: ",block_height
	print "getting all the blocks ..."
	blocks=[]
	for n in xrange(nblocks): #get all the image blocks
		blocks+=[get_block(im,n,block_width,block_height)]

	print "shuffling ..."
	#shuffle the order of the blocks
	new_order=range(nblocks)
	for n in xrange(nshuffle):
		random.shuffle(new_order)

	print "building final image ..."
	new_image=im.copy()
	for n in xrange(nblocks):
		#define the target box where to paste the new block
		i=(new_order[n]%grid_width_dim)*block_width				#i,j -> upper left point of the target image
		j=(new_order[n]/grid_width_dim)*block_height
		box = (i,j,i+block_width,j+block_height)	

		#paste it	
		new_image.paste(blocks[n],box)

	return new_image

#get a block of the image
def get_block(im,n,block_width,block_height):

	width=im.size[0]

	grid_width_dim=width/block_width						#dimension of the grid

	i=(n%grid_width_dim)*block_width						#i,j -> upper left point of the target block
	j=(n/grid_width_dim)*block_height

	box = (i,j,i+block_width,j+block_height)
	block_im = im.crop(box)
	return block_im

#set random seed based on the given password
def set_seed(password):
	passValue=0
	for ch in password:					
		passValue=passValue+ord(ch)
	random.seed(passValue)


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Sliding Puzzle',epilog="A fun toy.")
	parser.add_argument("-f","--filename",nargs=1,help="input filename",required=True)
	parser.add_argument("-p","--password",nargs=1,help="key for the random generator",default="yOs0ZaKpiS")
	parser.add_argument("-n","--nshuffle",nargs=1,help="number of times to shuffle the blocks (>0)",type=int,default=[1])
	parser.add_argument("-g","--granularity",nargs=1,help="granularity to be used (>0):  a bigger value means bigger blocks, default=1",type=int,default=[1])
	parser.add_argument("-u","--unpuzzle",help="unpuzzle the image",action='store_true',default=False)
	parser.add_argument("-s","--save",help="save the output image",action='store_true',default=False)

	args=vars(parser.parse_args())
	filename=args['filename'][0]
	password=args['password'][0]
	nshuffle=args['nshuffle'][0]
	granularity=args['granularity'][0]
	unpuzzle=args['unpuzzle']
	save=args['save']

	if nshuffle<1:
		parser.print_help()
		sys.exit()
	if granularity<1:
		parser.print_help()
		sys.exit()

	try:
		im=Image.open(filename)
	except Exception, e:
		print "An error has ocurred: %s" %e
		sys.exit()

	if unpuzzle:
		new_image=scramble_blocks(im,granularity,password,nshuffle)
	else:
		new_image=unscramble_blocks(im,granularity,password,nshuffle)
	new_image.show()

	if save and not unpuzzle:
		print "saving to "+filename.split(".")[0]+"_puzzled.png ..."
		new_image.save(filename.split(".")[0]+"_puzzled.png")
	elif save and unpuzzle:
		print "saving to "+filename.split(".")[0]+"_unpuzzled.png ..."
		new_image.save(filename.split(".")[0]+"_unpuzzled.png")