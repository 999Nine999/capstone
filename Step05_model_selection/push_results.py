def push_results(id, model, flavor, score):

	'''
	As an example, a cross validation for a RandomForestClassifier result would be push_results('rfcv', 'RandomForestClassifier', 'CV', 0.50)

	'''

	import pickle

	try:
		infile = open('../data/model_results/model_results.pickle','rb')
		results_dict = pickle.load(infile)
		infile.close()

	except:
		results_dict = {}

	results_dict.update({id: [model, flavor, score]})

	pickle_out = open('../data/model_results/model_results.pickle', 'wb')
	pickle.dump(results_dict, pickle_out)
	pickle_out.close()