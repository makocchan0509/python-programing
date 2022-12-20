from SampleRepository import DependencyInjector, AbstractSampleRepository

injector = DependencyInjector()
repo = injector.resolve(AbstractSampleRepository)
repo.get('abc_doc', 'abc_key')
repo.update({'abc_field': 100})
repo.insert('abc_doc', 'abc_key', {'abc_field': 100})
