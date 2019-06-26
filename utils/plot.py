import matplotlib.pyplot as plt

def plot(env, plot_list):
	if plot_list != None:
		for plot in plot_list:
			if plot == 'population':
				plt.plot(env.population_size)
				plt.show()
			if plot == 'speed':
				x = [blob.speed for blob in env.blobs]
				y = axe_y(env.blobs,x,plot)
				plt.bar(x,y)
				plt.xlabel('speed')
				plt.show()
			
			if plot == 'size':
				x = [blob.size for blob in env.blobs]
				y = axe_y(env.blobs,x,plot)
				plt.bar(x, y)
				plt.xlabel('size')
				plt.show()

			if plot == 'sense':
				x = [blob.sense for blob in env.blobs]
				y = axe_y(env.blobs,x,plot)
				plt.bar(x, y)
				plt.xlabel('sense')
				plt.show()

def axe_y(blobs ,trait_list, trait_type):
	return [len(list(filter(lambda blob: eval('blob.'+trait_type) == trait, blobs))) for trait in trait_list]