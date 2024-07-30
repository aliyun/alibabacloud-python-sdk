# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class Address(TeaModel):
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        district: str = None,
        language: str = None,
        province: str = None,
        township: str = None,
    ):
        self.address_line = address_line
        self.city = city
        self.country = country
        self.district = district
        self.language = language
        self.province = province
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.district is not None:
            result['District'] = self.district
        if self.language is not None:
            result['Language'] = self.language
        if self.province is not None:
            result['Province'] = self.province
        if self.township is not None:
            result['Township'] = self.township
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Township') is not None:
            self.township = m.get('Township')
        return self


class AddressForStory(TeaModel):
    def __init__(
        self,
        city: str = None,
        country: str = None,
        district: str = None,
        province: str = None,
        township: str = None,
    ):
        self.city = city
        self.country = country
        self.district = district
        self.province = province
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.district is not None:
            result['District'] = self.district
        if self.province is not None:
            result['Province'] = self.province
        if self.township is not None:
            result['Township'] = self.township
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Township') is not None:
            self.township = m.get('Township')
        return self


class MetaData(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        provider: str = None,
        version: str = None,
    ):
        self.identifier = identifier
        self.provider = provider
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class Property(TeaModel):
    def __init__(
        self,
        items_type: str = None,
        name: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.items_type = items_type
        self.name = name
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items_type is not None:
            result['ItemsType'] = self.items_type
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemsType') is not None:
            self.items_type = m.get('ItemsType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class CustomParams(TeaModel):
    def __init__(
        self,
        name: str = None,
        properties: List[Property] = None,
    ):
        self.name = name
        self.properties = properties

    def validate(self):
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = Property()
                self.properties.append(temp_model.from_map(k))
        return self


class Spec(TeaModel):
    def __init__(
        self,
        backbone: CustomParams = None,
        class_num: int = None,
        head: CustomParams = None,
        input_channel: int = None,
        loss: CustomParams = None,
        name: str = None,
        neck: CustomParams = None,
        num_landmarks: int = None,
        pretrained_path: str = None,
    ):
        self.backbone = backbone
        self.class_num = class_num
        self.head = head
        self.input_channel = input_channel
        self.loss = loss
        # This parameter is required.
        self.name = name
        self.neck = neck
        self.num_landmarks = num_landmarks
        self.pretrained_path = pretrained_path

    def validate(self):
        if self.backbone:
            self.backbone.validate()
        if self.head:
            self.head.validate()
        if self.loss:
            self.loss.validate()
        if self.neck:
            self.neck.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backbone is not None:
            result['Backbone'] = self.backbone.to_map()
        if self.class_num is not None:
            result['ClassNum'] = self.class_num
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.input_channel is not None:
            result['InputChannel'] = self.input_channel
        if self.loss is not None:
            result['Loss'] = self.loss.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.neck is not None:
            result['Neck'] = self.neck.to_map()
        if self.num_landmarks is not None:
            result['NumLandmarks'] = self.num_landmarks
        if self.pretrained_path is not None:
            result['PretrainedPath'] = self.pretrained_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backbone') is not None:
            temp_model = CustomParams()
            self.backbone = temp_model.from_map(m['Backbone'])
        if m.get('ClassNum') is not None:
            self.class_num = m.get('ClassNum')
        if m.get('Head') is not None:
            temp_model = CustomParams()
            self.head = temp_model.from_map(m['Head'])
        if m.get('InputChannel') is not None:
            self.input_channel = m.get('InputChannel')
        if m.get('Loss') is not None:
            temp_model = CustomParams()
            self.loss = temp_model.from_map(m['Loss'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Neck') is not None:
            temp_model = CustomParams()
            self.neck = temp_model.from_map(m['Neck'])
        if m.get('NumLandmarks') is not None:
            self.num_landmarks = m.get('NumLandmarks')
        if m.get('PretrainedPath') is not None:
            self.pretrained_path = m.get('PretrainedPath')
        return self


class ModelSpecification(TeaModel):
    def __init__(
        self,
        meta_data: MetaData = None,
        spec: Spec = None,
    ):
        # This parameter is required.
        self.meta_data = meta_data
        # This parameter is required.
        self.spec = spec

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaData') is not None:
            temp_model = MetaData()
            self.meta_data = temp_model.from_map(m['MetaData'])
        if m.get('Spec') is not None:
            temp_model = Spec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class Optimization(TeaModel):
    def __init__(
        self,
        learning_rate: float = None,
        optimizer: str = None,
    ):
        self.learning_rate = learning_rate
        self.optimizer = optimizer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.learning_rate is not None:
            result['LearningRate'] = self.learning_rate
        if self.optimizer is not None:
            result['Optimizer'] = self.optimizer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LearningRate') is not None:
            self.learning_rate = m.get('LearningRate')
        if m.get('Optimizer') is not None:
            self.optimizer = m.get('Optimizer')
        return self


class Schedule(TeaModel):
    def __init__(
        self,
        gamma: float = None,
        lrscheduler: str = None,
        step_size: int = None,
    ):
        self.gamma = gamma
        self.lrscheduler = lrscheduler
        self.step_size = step_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gamma is not None:
            result['Gamma'] = self.gamma
        if self.lrscheduler is not None:
            result['LRScheduler'] = self.lrscheduler
        if self.step_size is not None:
            result['StepSize'] = self.step_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gamma') is not None:
            self.gamma = m.get('Gamma')
        if m.get('LRScheduler') is not None:
            self.lrscheduler = m.get('LRScheduler')
        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')
        return self


class Hyperparameters(TeaModel):
    def __init__(
        self,
        backup_interval: int = None,
        batch_size: int = None,
        data_loader_workers: int = None,
        evaluator: CustomParams = None,
        input_size: List[int] = None,
        max_epoch: int = None,
        optimization: Optimization = None,
        schedule: Schedule = None,
    ):
        self.backup_interval = backup_interval
        self.batch_size = batch_size
        self.data_loader_workers = data_loader_workers
        # This parameter is required.
        self.evaluator = evaluator
        # This parameter is required.
        self.input_size = input_size
        self.max_epoch = max_epoch
        self.optimization = optimization
        self.schedule = schedule

    def validate(self):
        if self.evaluator:
            self.evaluator.validate()
        if self.optimization:
            self.optimization.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.data_loader_workers is not None:
            result['DataLoaderWorkers'] = self.data_loader_workers
        if self.evaluator is not None:
            result['Evaluator'] = self.evaluator.to_map()
        if self.input_size is not None:
            result['InputSize'] = self.input_size
        if self.max_epoch is not None:
            result['MaxEpoch'] = self.max_epoch
        if self.optimization is not None:
            result['Optimization'] = self.optimization.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('DataLoaderWorkers') is not None:
            self.data_loader_workers = m.get('DataLoaderWorkers')
        if m.get('Evaluator') is not None:
            temp_model = CustomParams()
            self.evaluator = temp_model.from_map(m['Evaluator'])
        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')
        if m.get('MaxEpoch') is not None:
            self.max_epoch = m.get('MaxEpoch')
        if m.get('Optimization') is not None:
            temp_model = Optimization()
            self.optimization = temp_model.from_map(m['Optimization'])
        if m.get('Schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        return self


class Resource(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        ecsinstance: str = None,
        gpumodel: str = None,
        gpunum: int = None,
        name: str = None,
        ram: int = None,
    ):
        self.cpu = cpu
        self.ecsinstance = ecsinstance
        self.gpumodel = gpumodel
        self.gpunum = gpunum
        self.name = name
        self.ram = ram

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.ecsinstance is not None:
            result['ECSInstance'] = self.ecsinstance
        if self.gpumodel is not None:
            result['GPUModel'] = self.gpumodel
        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum
        if self.name is not None:
            result['Name'] = self.name
        if self.ram is not None:
            result['RAM'] = self.ram
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('ECSInstance') is not None:
            self.ecsinstance = m.get('ECSInstance')
        if m.get('GPUModel') is not None:
            self.gpumodel = m.get('GPUModel')
        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RAM') is not None:
            self.ram = m.get('RAM')
        return self


class Runtime(TeaModel):
    def __init__(
        self,
        hyperparameters: Hyperparameters = None,
        resource: Resource = None,
    ):
        # This parameter is required.
        self.hyperparameters = hyperparameters
        # This parameter is required.
        self.resource = resource

    def validate(self):
        if self.hyperparameters:
            self.hyperparameters.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hyperparameters is not None:
            result['Hyperparameters'] = self.hyperparameters.to_map()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hyperparameters') is not None:
            temp_model = Hyperparameters()
            self.hyperparameters = temp_model.from_map(m['Hyperparameters'])
        if m.get('Resource') is not None:
            temp_model = Resource()
            self.resource = temp_model.from_map(m['Resource'])
        return self


class TrainingSpecification(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        endpoint: str = None,
        model_specification: ModelSpecification = None,
        runtime: Runtime = None,
        source_uri: str = None,
        target_uri: str = None,
        transforms: List[CustomParams] = None,
        validation_source_uri: str = None,
        validation_split: float = None,
    ):
        self.dataset_name = dataset_name
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.model_specification = model_specification
        # This parameter is required.
        self.runtime = runtime
        # This parameter is required.
        self.source_uri = source_uri
        # This parameter is required.
        self.target_uri = target_uri
        self.transforms = transforms
        self.validation_source_uri = validation_source_uri
        self.validation_split = validation_split

    def validate(self):
        if self.model_specification:
            self.model_specification.validate()
        if self.runtime:
            self.runtime.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.model_specification is not None:
            result['ModelSpecification'] = self.model_specification.to_map()
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        if self.validation_source_uri is not None:
            result['ValidationSourceURI'] = self.validation_source_uri
        if self.validation_split is not None:
            result['ValidationSplit'] = self.validation_split
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ModelSpecification') is not None:
            temp_model = ModelSpecification()
            self.model_specification = temp_model.from_map(m['ModelSpecification'])
        if m.get('Runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['Runtime'])
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = CustomParams()
                self.transforms.append(temp_model.from_map(k))
        if m.get('ValidationSourceURI') is not None:
            self.validation_source_uri = m.get('ValidationSourceURI')
        if m.get('ValidationSplit') is not None:
            self.validation_split = m.get('ValidationSplit')
        return self


class AlgorithmDefinition(TeaModel):
    def __init__(
        self,
        algorithm_definition_id: str = None,
        create_time: str = None,
        custom_labels: List[Dict[str, str]] = None,
        description: str = None,
        name: str = None,
        owner_id: str = None,
        project_name: str = None,
        training_specification: TrainingSpecification = None,
        update_time: str = None,
    ):
        self.algorithm_definition_id = algorithm_definition_id
        self.create_time = create_time
        self.custom_labels = custom_labels
        self.description = description
        self.name = name
        self.owner_id = owner_id
        self.project_name = project_name
        self.training_specification = training_specification
        self.update_time = update_time

    def validate(self):
        if self.training_specification:
            self.training_specification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_definition_id is not None:
            result['AlgorithmDefinitionId'] = self.algorithm_definition_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.training_specification is not None:
            result['TrainingSpecification'] = self.training_specification.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmDefinitionId') is not None:
            self.algorithm_definition_id = m.get('AlgorithmDefinitionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TrainingSpecification') is not None:
            temp_model = TrainingSpecification()
            self.training_specification = temp_model.from_map(m['TrainingSpecification'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class App(TeaModel):
    def __init__(
        self,
        app_description: str = None,
        app_id: str = None,
        app_key: str = None,
        app_name: str = None,
        app_region: int = None,
        app_type: int = None,
        english_name: str = None,
        owner_id: str = None,
        package_name: str = None,
    ):
        self.app_description = app_description
        self.app_id = app_id
        self.app_key = app_key
        self.app_name = app_name
        self.app_region = app_region
        self.app_type = app_type
        self.english_name = english_name
        self.owner_id = owner_id
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_region is not None:
            result['AppRegion'] = self.app_region
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRegion') is not None:
            self.app_region = m.get('AppRegion')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class AssumeRoleChainNode(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        role: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.owner_id = owner_id
        # This parameter is required.
        self.role = role
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AssumeRoleChain(TeaModel):
    def __init__(
        self,
        chain: List[AssumeRoleChainNode] = None,
        policy: str = None,
    ):
        self.chain = chain
        self.policy = policy

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = AssumeRoleChainNode()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class AudioStream(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        channel_layout: str = None,
        channels: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: float = None,
        frame_count: int = None,
        index: int = None,
        language: str = None,
        lyric: str = None,
        sample_format: str = None,
        sample_rate: int = None,
        start_time: float = None,
        time_base: str = None,
    ):
        self.bitrate = bitrate
        self.channel_layout = channel_layout
        self.channels = channels
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.duration = duration
        self.frame_count = frame_count
        self.index = index
        self.language = language
        self.lyric = lyric
        self.sample_format = sample_format
        self.sample_rate = sample_rate
        self.start_time = start_time
        self.time_base = time_base

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        return self


class Binding(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_name: str = None,
        phase: str = None,
        project_name: str = None,
        reason: str = None,
        state: str = None,
        uri: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.dataset_name = dataset_name
        self.phase = phase
        self.project_name = project_name
        self.reason = reason
        self.state = state
        self.uri = uri
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.state is not None:
            result['State'] = self.state
        if self.uri is not None:
            result['URI'] = self.uri
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class PointInt64(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class Boundary(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        polygon: List[PointInt64] = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.polygon = polygon
        self.top = top
        self.width = width

    def validate(self):
        if self.polygon:
            for k in self.polygon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        result['Polygon'] = []
        if self.polygon is not None:
            for k in self.polygon:
                result['Polygon'].append(k.to_map() if k else None)
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        self.polygon = []
        if m.get('Polygon') is not None:
            for k in m.get('Polygon'):
                temp_model = PointInt64()
                self.polygon.append(temp_model.from_map(k))
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class Body(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
    ):
        self.boundary = boundary
        self.confidence = confidence

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class LicensePlate(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
        content: str = None,
    ):
        self.boundary = boundary
        self.confidence = confidence
        self.content = content

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class Car(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        car_color: str = None,
        car_color_confidence: float = None,
        car_type: str = None,
        car_type_confidence: float = None,
        confidence: float = None,
        license_plates: List[LicensePlate] = None,
    ):
        self.boundary = boundary
        self.car_color = car_color
        self.car_color_confidence = car_color_confidence
        self.car_type = car_type
        self.car_type_confidence = car_type_confidence
        self.confidence = confidence
        self.license_plates = license_plates

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.license_plates:
            for k in self.license_plates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.car_color is not None:
            result['CarColor'] = self.car_color
        if self.car_color_confidence is not None:
            result['CarColorConfidence'] = self.car_color_confidence
        if self.car_type is not None:
            result['CarType'] = self.car_type
        if self.car_type_confidence is not None:
            result['CarTypeConfidence'] = self.car_type_confidence
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        result['LicensePlates'] = []
        if self.license_plates is not None:
            for k in self.license_plates:
                result['LicensePlates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('CarColor') is not None:
            self.car_color = m.get('CarColor')
        if m.get('CarColorConfidence') is not None:
            self.car_color_confidence = m.get('CarColorConfidence')
        if m.get('CarType') is not None:
            self.car_type = m.get('CarType')
        if m.get('CarTypeConfidence') is not None:
            self.car_type_confidence = m.get('CarTypeConfidence')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        self.license_plates = []
        if m.get('LicensePlates') is not None:
            for k in m.get('LicensePlates'):
                temp_model = LicensePlate()
                self.license_plates.append(temp_model.from_map(k))
        return self


class ClusterForReqCoverFigures(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class ClusterForReqCover(TeaModel):
    def __init__(
        self,
        figures: List[ClusterForReqCoverFigures] = None,
    ):
        self.figures = figures

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = ClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k))
        return self


class ClusterForReq(TeaModel):
    def __init__(
        self,
        cover: ClusterForReqCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        name: str = None,
        object_id: str = None,
    ):
        self.cover = cover
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.name = name
        self.object_id = object_id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = ClusterForReqCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class Codes(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
        content: str = None,
        type: str = None,
    ):
        self.boundary = boundary
        self.confidence = confidence
        self.content = content
        self.type = type

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CredentialConfigChain(TeaModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role: str = None,
        role_type: str = None,
    ):
        self.assume_role_for = assume_role_for
        self.role = role
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        if self.role is not None:
            result['Role'] = self.role
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CredentialConfig(TeaModel):
    def __init__(
        self,
        chain: List[CredentialConfigChain] = None,
        policy: str = None,
        service_role: str = None,
    ):
        self.chain = chain
        self.policy = policy
        self.service_role = service_role

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = CredentialConfigChain()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        return self


class CroppingSuggestion(TeaModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        boundary: Boundary = None,
        confidence: float = None,
    ):
        self.aspect_ratio = aspect_ratio
        self.boundary = boundary
        self.confidence = confidence

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class FastFailPolicy(TeaModel):
    def __init__(
        self,
        action: str = None,
    ):
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class DataIngestionActions(TeaModel):
    def __init__(
        self,
        fast_fail_policy: FastFailPolicy = None,
        name: str = None,
        parameters: List[str] = None,
    ):
        self.fast_fail_policy = fast_fail_policy
        self.name = name
        self.parameters = parameters

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m['FastFailPolicy'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class MNS(TeaModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class RocketMQ(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        topic_name: str = None,
    ):
        self.instance_id = instance_id
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class DataIngestionNotification(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        mns: MNS = None,
        rocket_mq: RocketMQ = None,
        topic: str = None,
    ):
        self.endpoint = endpoint
        self.mns = mns
        self.rocket_mq = rocket_mq
        self.topic = topic

    def validate(self):
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        if m.get('RocketMQ') is not None:
            temp_model = RocketMQ()
            self.rocket_mq = temp_model.from_map(m['RocketMQ'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DataIngestionStatistic(TeaModel):
    def __init__(
        self,
        skip_files: int = None,
        submit_failure: int = None,
        submit_success: int = None,
    ):
        self.skip_files = skip_files
        self.submit_failure = submit_failure
        self.submit_success = submit_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_files is not None:
            result['SkipFiles'] = self.skip_files
        if self.submit_failure is not None:
            result['SubmitFailure'] = self.submit_failure
        if self.submit_success is not None:
            result['SubmitSuccess'] = self.submit_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipFiles') is not None:
            self.skip_files = m.get('SkipFiles')
        if m.get('SubmitFailure') is not None:
            self.submit_failure = m.get('SubmitFailure')
        if m.get('SubmitSuccess') is not None:
            self.submit_success = m.get('SubmitSuccess')
        return self


class InputOSS(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        match_expressions: List[str] = None,
        prefix: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        self.match_expressions = match_expressions
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class Input(TeaModel):
    def __init__(
        self,
        oss: InputOSS = None,
    ):
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSS') is not None:
            temp_model = InputOSS()
            self.oss = temp_model.from_map(m['OSS'])
        return self


class DataIngestion(TeaModel):
    def __init__(
        self,
        actions: List[DataIngestionActions] = None,
        create_time: str = None,
        error: str = None,
        id: str = None,
        input: Input = None,
        marker: str = None,
        notification: DataIngestionNotification = None,
        phase: str = None,
        service_role: str = None,
        state: str = None,
        statistic: DataIngestionStatistic = None,
        tags: Dict[str, Any] = None,
        update_time: str = None,
    ):
        self.actions = actions
        self.create_time = create_time
        self.error = error
        self.id = id
        self.input = input
        self.marker = marker
        self.notification = notification
        self.phase = phase
        self.service_role = service_role
        self.state = state
        self.statistic = statistic
        self.tags = tags
        self.update_time = update_time

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()
        if self.statistic:
            self.statistic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.state is not None:
            result['State'] = self.state
        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = DataIngestionActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Notification') is not None:
            temp_model = DataIngestionNotification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Statistic') is not None:
            temp_model = DataIngestionStatistic()
            self.statistic = temp_model.from_map(m['Statistic'])
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Dataset(TeaModel):
    def __init__(
        self,
        bind_count: int = None,
        create_time: str = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        file_count: int = None,
        project_name: str = None,
        template_id: str = None,
        total_file_size: int = None,
        update_time: str = None,
    ):
        self.bind_count = bind_count
        self.create_time = create_time
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.dataset_name = dataset_name
        self.description = description
        self.file_count = file_count
        self.project_name = project_name
        self.template_id = template_id
        self.total_file_size = total_file_size
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ElementContent(TeaModel):
    def __init__(
        self,
        content: str = None,
        time_range: List[int] = None,
        type: str = None,
        url: str = None,
    ):
        self.content = content
        self.time_range = time_range
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class Element(TeaModel):
    def __init__(
        self,
        element_contents: List[ElementContent] = None,
    ):
        self.element_contents = element_contents

    def validate(self):
        if self.element_contents:
            for k in self.element_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ElementContents'] = []
        if self.element_contents is not None:
            for k in self.element_contents:
                result['ElementContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.element_contents = []
        if m.get('ElementContents') is not None:
            for k in m.get('ElementContents'):
                temp_model = ElementContent()
                self.element_contents.append(temp_model.from_map(k))
        return self


class HeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class Figure(TeaModel):
    def __init__(
        self,
        age: int = None,
        age_sd: float = None,
        attractive: float = None,
        beard: str = None,
        beard_confidence: float = None,
        boundary: Boundary = None,
        emotion: str = None,
        emotion_confidence: float = None,
        face_quality: float = None,
        figure_cluster_confidence: float = None,
        figure_cluster_id: str = None,
        figure_confidence: float = None,
        figure_id: str = None,
        figure_type: str = None,
        gender: str = None,
        gender_confidence: float = None,
        glasses: str = None,
        glasses_confidence: float = None,
        hat: str = None,
        hat_confidence: float = None,
        head_pose: HeadPose = None,
        mask: str = None,
        mask_confidence: float = None,
        mouth: str = None,
        mouth_confidence: float = None,
        sharpness: float = None,
    ):
        self.age = age
        self.age_sd = age_sd
        self.attractive = attractive
        self.beard = beard
        self.beard_confidence = beard_confidence
        self.boundary = boundary
        self.emotion = emotion
        self.emotion_confidence = emotion_confidence
        self.face_quality = face_quality
        self.figure_cluster_confidence = figure_cluster_confidence
        self.figure_cluster_id = figure_cluster_id
        self.figure_confidence = figure_confidence
        self.figure_id = figure_id
        self.figure_type = figure_type
        self.gender = gender
        self.gender_confidence = gender_confidence
        self.glasses = glasses
        self.glasses_confidence = glasses_confidence
        self.hat = hat
        self.hat_confidence = hat_confidence
        self.head_pose = head_pose
        self.mask = mask
        self.mask_confidence = mask_confidence
        self.mouth = mouth
        self.mouth_confidence = mouth_confidence
        self.sharpness = sharpness

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.age_sd is not None:
            result['AgeSD'] = self.age_sd
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.figure_cluster_confidence is not None:
            result['FigureClusterConfidence'] = self.figure_cluster_confidence
        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id
        if self.figure_confidence is not None:
            result['FigureConfidence'] = self.figure_confidence
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.hat is not None:
            result['Hat'] = self.hat
        if self.hat_confidence is not None:
            result['HatConfidence'] = self.hat_confidence
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.mouth is not None:
            result['Mouth'] = self.mouth
        if self.mouth_confidence is not None:
            result['MouthConfidence'] = self.mouth_confidence
        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('AgeSD') is not None:
            self.age_sd = m.get('AgeSD')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('FigureClusterConfidence') is not None:
            self.figure_cluster_confidence = m.get('FigureClusterConfidence')
        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')
        if m.get('FigureConfidence') is not None:
            self.figure_confidence = m.get('FigureConfidence')
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Hat') is not None:
            self.hat = m.get('Hat')
        if m.get('HatConfidence') is not None:
            self.hat_confidence = m.get('HatConfidence')
        if m.get('HeadPose') is not None:
            temp_model = HeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Mouth') is not None:
            self.mouth = m.get('Mouth')
        if m.get('MouthConfidence') is not None:
            self.mouth_confidence = m.get('MouthConfidence')
        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')
        return self


class ImageScore(TeaModel):
    def __init__(
        self,
        overall_quality_score: float = None,
    ):
        self.overall_quality_score = overall_quality_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class OCRContents(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
        contents: str = None,
        language: str = None,
    ):
        self.boundary = boundary
        self.confidence = confidence
        self.contents = contents
        self.language = language

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class Image(TeaModel):
    def __init__(
        self,
        cropping_suggestions: List[CroppingSuggestion] = None,
        exif: str = None,
        image_height: int = None,
        image_score: ImageScore = None,
        image_width: int = None,
        ocrcontents: List[OCRContents] = None,
    ):
        self.cropping_suggestions = cropping_suggestions
        self.exif = exif
        self.image_height = image_height
        self.image_score = image_score
        self.image_width = image_width
        self.ocrcontents = ocrcontents

    def validate(self):
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        return self


class Label(TeaModel):
    def __init__(
        self,
        centric_score: float = None,
        label_confidence: float = None,
        label_level: int = None,
        label_name: str = None,
        language: str = None,
        parent_label_name: str = None,
    ):
        self.centric_score = centric_score
        self.label_confidence = label_confidence
        self.label_level = label_level
        self.label_name = label_name
        self.language = language
        self.parent_label_name = parent_label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centric_score is not None:
            result['CentricScore'] = self.centric_score
        if self.label_confidence is not None:
            result['LabelConfidence'] = self.label_confidence
        if self.label_level is not None:
            result['LabelLevel'] = self.label_level
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.language is not None:
            result['Language'] = self.language
        if self.parent_label_name is not None:
            result['ParentLabelName'] = self.parent_label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CentricScore') is not None:
            self.centric_score = m.get('CentricScore')
        if m.get('LabelConfidence') is not None:
            self.label_confidence = m.get('LabelConfidence')
        if m.get('LabelLevel') is not None:
            self.label_level = m.get('LabelLevel')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ParentLabelName') is not None:
            self.parent_label_name = m.get('ParentLabelName')
        return self


class SceneElement(TeaModel):
    def __init__(
        self,
        frame_times: List[int] = None,
        time_range: List[int] = None,
    ):
        self.frame_times = frame_times
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_times is not None:
            result['FrameTimes'] = self.frame_times
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameTimes') is not None:
            self.frame_times = m.get('FrameTimes')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class SubtitleStream(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        content: str = None,
        duration: float = None,
        height: int = None,
        index: int = None,
        language: str = None,
        start_time: float = None,
        width: int = None,
    ):
        self.bitrate = bitrate
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.content = content
        self.duration = duration
        self.height = height
        self.index = index
        self.language = language
        self.start_time = start_time
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.content is not None:
            result['Content'] = self.content
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class VideoStream(TeaModel):
    def __init__(
        self,
        average_frame_rate: str = None,
        bit_depth: int = None,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        color_primaries: str = None,
        color_range: str = None,
        color_space: str = None,
        color_transfer: str = None,
        display_aspect_ratio: str = None,
        duration: float = None,
        frame_count: int = None,
        frame_rate: str = None,
        has_bframes: int = None,
        height: int = None,
        index: int = None,
        language: str = None,
        level: int = None,
        pixel_format: str = None,
        profile: str = None,
        rotate: str = None,
        sample_aspect_ratio: str = None,
        start_time: float = None,
        time_base: str = None,
        width: int = None,
    ):
        self.average_frame_rate = average_frame_rate
        self.bit_depth = bit_depth
        self.bitrate = bitrate
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.color_primaries = color_primaries
        self.color_range = color_range
        self.color_space = color_space
        self.color_transfer = color_transfer
        self.display_aspect_ratio = display_aspect_ratio
        self.duration = duration
        self.frame_count = frame_count
        self.frame_rate = frame_rate
        self.has_bframes = has_bframes
        self.height = height
        self.index = index
        self.language = language
        self.level = level
        self.pixel_format = pixel_format
        self.profile = profile
        self.rotate = rotate
        self.sample_aspect_ratio = sample_aspect_ratio
        self.start_time = start_time
        self.time_base = time_base
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate
        if self.bit_depth is not None:
            result['BitDepth'] = self.bit_depth
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.color_primaries is not None:
            result['ColorPrimaries'] = self.color_primaries
        if self.color_range is not None:
            result['ColorRange'] = self.color_range
        if self.color_space is not None:
            result['ColorSpace'] = self.color_space
        if self.color_transfer is not None:
            result['ColorTransfer'] = self.color_transfer
        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.level is not None:
            result['Level'] = self.level
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')
        if m.get('BitDepth') is not None:
            self.bit_depth = m.get('BitDepth')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('ColorPrimaries') is not None:
            self.color_primaries = m.get('ColorPrimaries')
        if m.get('ColorRange') is not None:
            self.color_range = m.get('ColorRange')
        if m.get('ColorSpace') is not None:
            self.color_space = m.get('ColorSpace')
        if m.get('ColorTransfer') is not None:
            self.color_transfer = m.get('ColorTransfer')
        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class File(TeaModel):
    def __init__(
        self,
        access_control_allow_origin: str = None,
        access_control_request_method: str = None,
        addresses: List[Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        audio_covers: List[Image] = None,
        audio_streams: List[AudioStream] = None,
        bitrate: int = None,
        cache_control: str = None,
        composer: str = None,
        content_disposition: str = None,
        content_encoding: str = None,
        content_language: str = None,
        content_md_5: str = None,
        content_type: str = None,
        create_time: str = None,
        cropping_suggestions: List[CroppingSuggestion] = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        duration: float = None,
        etag: str = None,
        exif: str = None,
        elements: List[Element] = None,
        figure_count: int = None,
        figures: List[Figure] = None,
        file_access_time: str = None,
        file_create_time: str = None,
        file_hash: str = None,
        file_modified_time: str = None,
        filename: str = None,
        format_long_name: str = None,
        format_name: str = None,
        image_height: int = None,
        image_score: ImageScore = None,
        image_width: int = None,
        labels: List[Label] = None,
        language: str = None,
        lat_long: str = None,
        media_type: str = None,
        ocrcontents: List[OCRContents] = None,
        ocrtexts: str = None,
        osscrc64: str = None,
        ossdelete_marker: str = None,
        ossexpiration: str = None,
        ossobject_type: str = None,
        ossstorage_class: str = None,
        osstagging: Dict[str, Any] = None,
        osstagging_count: int = None,
        ossuri: str = None,
        ossuser_meta: Dict[str, Any] = None,
        ossversion_id: str = None,
        object_acl: str = None,
        object_id: str = None,
        object_status: str = None,
        object_type: str = None,
        orientation: int = None,
        owner_id: str = None,
        page_count: int = None,
        performer: str = None,
        produce_time: str = None,
        program_count: int = None,
        project_name: str = None,
        reason: str = None,
        scene_elements: List[SceneElement] = None,
        semantic_types: List[str] = None,
        server_side_data_encryption: str = None,
        server_side_encryption: str = None,
        server_side_encryption_customer_algorithm: str = None,
        server_side_encryption_key_id: str = None,
        size: int = None,
        start_time: float = None,
        stream_count: int = None,
        subtitles: List[SubtitleStream] = None,
        timezone: str = None,
        title: str = None,
        travel_cluster_id: str = None,
        uri: str = None,
        update_time: str = None,
        video_height: int = None,
        video_streams: List[VideoStream] = None,
        video_width: int = None,
    ):
        self.access_control_allow_origin = access_control_allow_origin
        self.access_control_request_method = access_control_request_method
        self.addresses = addresses
        self.album = album
        self.album_artist = album_artist
        self.artist = artist
        self.audio_covers = audio_covers
        self.audio_streams = audio_streams
        self.bitrate = bitrate
        self.cache_control = cache_control
        self.composer = composer
        self.content_disposition = content_disposition
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_md_5 = content_md_5
        self.content_type = content_type
        self.create_time = create_time
        self.cropping_suggestions = cropping_suggestions
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.duration = duration
        self.etag = etag
        self.exif = exif
        self.elements = elements
        self.figure_count = figure_count
        self.figures = figures
        self.file_access_time = file_access_time
        self.file_create_time = file_create_time
        self.file_hash = file_hash
        self.file_modified_time = file_modified_time
        self.filename = filename
        self.format_long_name = format_long_name
        self.format_name = format_name
        self.image_height = image_height
        self.image_score = image_score
        self.image_width = image_width
        self.labels = labels
        self.language = language
        self.lat_long = lat_long
        self.media_type = media_type
        self.ocrcontents = ocrcontents
        self.ocrtexts = ocrtexts
        self.osscrc64 = osscrc64
        self.ossdelete_marker = ossdelete_marker
        self.ossexpiration = ossexpiration
        self.ossobject_type = ossobject_type
        self.ossstorage_class = ossstorage_class
        self.osstagging = osstagging
        self.osstagging_count = osstagging_count
        self.ossuri = ossuri
        self.ossuser_meta = ossuser_meta
        self.ossversion_id = ossversion_id
        self.object_acl = object_acl
        self.object_id = object_id
        self.object_status = object_status
        self.object_type = object_type
        self.orientation = orientation
        self.owner_id = owner_id
        self.page_count = page_count
        self.performer = performer
        self.produce_time = produce_time
        self.program_count = program_count
        self.project_name = project_name
        self.reason = reason
        self.scene_elements = scene_elements
        self.semantic_types = semantic_types
        self.server_side_data_encryption = server_side_data_encryption
        self.server_side_encryption = server_side_encryption
        self.server_side_encryption_customer_algorithm = server_side_encryption_customer_algorithm
        self.server_side_encryption_key_id = server_side_encryption_key_id
        self.size = size
        self.start_time = start_time
        self.stream_count = stream_count
        self.subtitles = subtitles
        self.timezone = timezone
        self.title = title
        self.travel_cluster_id = travel_cluster_id
        self.uri = uri
        self.update_time = update_time
        self.video_height = video_height
        self.video_streams = video_streams
        self.video_width = video_width

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.audio_covers:
            for k in self.audio_covers:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()
        if self.scene_elements:
            for k in self.scene_elements:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_control_request_method is not None:
            result['AccessControlRequestMethod'] = self.access_control_request_method
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        result['AudioCovers'] = []
        if self.audio_covers is not None:
            for k in self.audio_covers:
                result['AudioCovers'].append(k.to_map() if k else None)
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.cache_control is not None:
            result['CacheControl'] = self.cache_control
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.content_disposition is not None:
            result['ContentDisposition'] = self.content_disposition
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_language is not None:
            result['ContentLanguage'] = self.content_language
        if self.content_md_5 is not None:
            result['ContentMd5'] = self.content_md_5
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.exif is not None:
            result['EXIF'] = self.exif
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.figure_count is not None:
            result['FigureCount'] = self.figure_count
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        if self.file_access_time is not None:
            result['FileAccessTime'] = self.file_access_time
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_modified_time is not None:
            result['FileModifiedTime'] = self.file_modified_time
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.language is not None:
            result['Language'] = self.language
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.ocrtexts is not None:
            result['OCRTexts'] = self.ocrtexts
        if self.osscrc64 is not None:
            result['OSSCRC64'] = self.osscrc64
        if self.ossdelete_marker is not None:
            result['OSSDeleteMarker'] = self.ossdelete_marker
        if self.ossexpiration is not None:
            result['OSSExpiration'] = self.ossexpiration
        if self.ossobject_type is not None:
            result['OSSObjectType'] = self.ossobject_type
        if self.ossstorage_class is not None:
            result['OSSStorageClass'] = self.ossstorage_class
        if self.osstagging is not None:
            result['OSSTagging'] = self.osstagging
        if self.osstagging_count is not None:
            result['OSSTaggingCount'] = self.osstagging_count
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.ossuser_meta is not None:
            result['OSSUserMeta'] = self.ossuser_meta
        if self.ossversion_id is not None:
            result['OSSVersionId'] = self.ossversion_id
        if self.object_acl is not None:
            result['ObjectACL'] = self.object_acl
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_status is not None:
            result['ObjectStatus'] = self.object_status
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.program_count is not None:
            result['ProgramCount'] = self.program_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reason is not None:
            result['Reason'] = self.reason
        result['SceneElements'] = []
        if self.scene_elements is not None:
            for k in self.scene_elements:
                result['SceneElements'].append(k.to_map() if k else None)
        if self.semantic_types is not None:
            result['SemanticTypes'] = self.semantic_types
        if self.server_side_data_encryption is not None:
            result['ServerSideDataEncryption'] = self.server_side_data_encryption
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.server_side_encryption_customer_algorithm is not None:
            result['ServerSideEncryptionCustomerAlgorithm'] = self.server_side_encryption_customer_algorithm
        if self.server_side_encryption_key_id is not None:
            result['ServerSideEncryptionKeyId'] = self.server_side_encryption_key_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.title is not None:
            result['Title'] = self.title
        if self.travel_cluster_id is not None:
            result['TravelClusterId'] = self.travel_cluster_id
        if self.uri is not None:
            result['URI'] = self.uri
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessControlRequestMethod') is not None:
            self.access_control_request_method = m.get('AccessControlRequestMethod')
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        self.audio_covers = []
        if m.get('AudioCovers') is not None:
            for k in m.get('AudioCovers'):
                temp_model = Image()
                self.audio_covers.append(temp_model.from_map(k))
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CacheControl') is not None:
            self.cache_control = m.get('CacheControl')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('ContentDisposition') is not None:
            self.content_disposition = m.get('ContentDisposition')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentLanguage') is not None:
            self.content_language = m.get('ContentLanguage')
        if m.get('ContentMd5') is not None:
            self.content_md_5 = m.get('ContentMd5')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = Element()
                self.elements.append(temp_model.from_map(k))
        if m.get('FigureCount') is not None:
            self.figure_count = m.get('FigureCount')
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = Figure()
                self.figures.append(temp_model.from_map(k))
        if m.get('FileAccessTime') is not None:
            self.file_access_time = m.get('FileAccessTime')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileModifiedTime') is not None:
            self.file_modified_time = m.get('FileModifiedTime')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('OCRTexts') is not None:
            self.ocrtexts = m.get('OCRTexts')
        if m.get('OSSCRC64') is not None:
            self.osscrc64 = m.get('OSSCRC64')
        if m.get('OSSDeleteMarker') is not None:
            self.ossdelete_marker = m.get('OSSDeleteMarker')
        if m.get('OSSExpiration') is not None:
            self.ossexpiration = m.get('OSSExpiration')
        if m.get('OSSObjectType') is not None:
            self.ossobject_type = m.get('OSSObjectType')
        if m.get('OSSStorageClass') is not None:
            self.ossstorage_class = m.get('OSSStorageClass')
        if m.get('OSSTagging') is not None:
            self.osstagging = m.get('OSSTagging')
        if m.get('OSSTaggingCount') is not None:
            self.osstagging_count = m.get('OSSTaggingCount')
        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')
        if m.get('OSSUserMeta') is not None:
            self.ossuser_meta = m.get('OSSUserMeta')
        if m.get('OSSVersionId') is not None:
            self.ossversion_id = m.get('OSSVersionId')
        if m.get('ObjectACL') is not None:
            self.object_acl = m.get('ObjectACL')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectStatus') is not None:
            self.object_status = m.get('ObjectStatus')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.scene_elements = []
        if m.get('SceneElements') is not None:
            for k in m.get('SceneElements'):
                temp_model = SceneElement()
                self.scene_elements.append(temp_model.from_map(k))
        if m.get('SemanticTypes') is not None:
            self.semantic_types = m.get('SemanticTypes')
        if m.get('ServerSideDataEncryption') is not None:
            self.server_side_data_encryption = m.get('ServerSideDataEncryption')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('ServerSideEncryptionCustomerAlgorithm') is not None:
            self.server_side_encryption_customer_algorithm = m.get('ServerSideEncryptionCustomerAlgorithm')
        if m.get('ServerSideEncryptionKeyId') is not None:
            self.server_side_encryption_key_id = m.get('ServerSideEncryptionKeyId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TravelClusterId') is not None:
            self.travel_cluster_id = m.get('TravelClusterId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class FigureCluster(TeaModel):
    def __init__(
        self,
        average_age: float = None,
        cover: File = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        face_count: int = None,
        gender: str = None,
        image_count: int = None,
        max_age: float = None,
        meta_lock_version: int = None,
        min_age: float = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        update_time: str = None,
        video_count: int = None,
    ):
        self.average_age = average_age
        self.cover = cover
        self.create_time = create_time
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.face_count = face_count
        self.gender = gender
        self.image_count = image_count
        self.max_age = max_age
        self.meta_lock_version = meta_lock_version
        self.min_age = min_age
        self.name = name
        self.object_id = object_id
        self.object_type = object_type
        self.owner_id = owner_id
        self.project_name = project_name
        self.update_time = update_time
        self.video_count = video_count

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_age is not None:
            result['AverageAge'] = self.average_age
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.meta_lock_version is not None:
            result['MetaLockVersion'] = self.meta_lock_version
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageAge') is not None:
            self.average_age = m.get('AverageAge')
        if m.get('Cover') is not None:
            temp_model = File()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('MetaLockVersion') is not None:
            self.meta_lock_version = m.get('MetaLockVersion')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        return self


class FigureClusterForReqCoverFigures(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class FigureClusterForReqCover(TeaModel):
    def __init__(
        self,
        figures: List[FigureClusterForReqCoverFigures] = None,
    ):
        self.figures = figures

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = FigureClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k))
        return self


class FigureClusterForReq(TeaModel):
    def __init__(
        self,
        cover: FigureClusterForReqCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        meta_lock_version: int = None,
        name: str = None,
        object_id: str = None,
    ):
        self.cover = cover
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.meta_lock_version = meta_lock_version
        self.name = name
        self.object_id = object_id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.meta_lock_version is not None:
            result['MetaLockVersion'] = self.meta_lock_version
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = FigureClusterForReqCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('MetaLockVersion') is not None:
            self.meta_lock_version = m.get('MetaLockVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class InputFileFigures(TeaModel):
    def __init__(
        self,
        figure_cluster_id: str = None,
        figure_id: str = None,
        figure_type: str = None,
    ):
        self.figure_cluster_id = figure_cluster_id
        self.figure_id = figure_id
        self.figure_type = figure_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        return self


class InputFile(TeaModel):
    def __init__(
        self,
        addresses: List[Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        composer: str = None,
        content_type: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        figures: List[InputFileFigures] = None,
        file_hash: str = None,
        labels: List[Label] = None,
        lat_long: str = None,
        media_type: str = None,
        ossuri: str = None,
        performer: str = None,
        produce_time: str = None,
        title: str = None,
        uri: str = None,
    ):
        self.addresses = addresses
        self.album = album
        self.album_artist = album_artist
        self.artist = artist
        self.composer = composer
        self.content_type = content_type
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.figures = figures
        self.file_hash = file_hash
        self.labels = labels
        self.lat_long = lat_long
        self.media_type = media_type
        self.ossuri = ossuri
        self.performer = performer
        self.produce_time = produce_time
        self.title = title
        self.uri = uri

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.title is not None:
            result['Title'] = self.title
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = InputFileFigures()
                self.figures.append(temp_model.from_map(k))
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class KdtreeOption(TeaModel):
    def __init__(
        self,
        compression_level: int = None,
        library_name: str = None,
        quantization_bits: int = None,
    ):
        self.compression_level = compression_level
        self.library_name = library_name
        self.quantization_bits = quantization_bits

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compression_level is not None:
            result['CompressionLevel'] = self.compression_level
        if self.library_name is not None:
            result['LibraryName'] = self.library_name
        if self.quantization_bits is not None:
            result['QuantizationBits'] = self.quantization_bits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressionLevel') is not None:
            self.compression_level = m.get('CompressionLevel')
        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')
        if m.get('QuantizationBits') is not None:
            self.quantization_bits = m.get('QuantizationBits')
        return self


class KeyValuePair(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LocationDateCluster(TeaModel):
    def __init__(
        self,
        addresses: List[Address] = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        location_date_cluster_end_time: str = None,
        location_date_cluster_level: str = None,
        location_date_cluster_start_time: str = None,
        object_id: str = None,
        title: str = None,
        update_time: str = None,
    ):
        self.addresses = addresses
        self.create_time = create_time
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.location_date_cluster_end_time = location_date_cluster_end_time
        self.location_date_cluster_level = location_date_cluster_level
        self.location_date_cluster_start_time = location_date_cluster_start_time
        self.object_id = object_id
        self.title = title
        self.update_time = update_time

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.location_date_cluster_end_time is not None:
            result['LocationDateClusterEndTime'] = self.location_date_cluster_end_time
        if self.location_date_cluster_level is not None:
            result['LocationDateClusterLevel'] = self.location_date_cluster_level
        if self.location_date_cluster_start_time is not None:
            result['LocationDateClusterStartTime'] = self.location_date_cluster_start_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('LocationDateClusterEndTime') is not None:
            self.location_date_cluster_end_time = m.get('LocationDateClusterEndTime')
        if m.get('LocationDateClusterLevel') is not None:
            self.location_date_cluster_level = m.get('LocationDateClusterLevel')
        if m.get('LocationDateClusterStartTime') is not None:
            self.location_date_cluster_start_time = m.get('LocationDateClusterStartTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Message(TeaModel):
    def __init__(
        self,
        assistant_type: str = None,
        content: str = None,
        create_time: str = None,
        dataset_name: str = None,
        language: str = None,
        regenerate: bool = None,
        reply: str = None,
        score: float = None,
        source_uri: str = None,
        suggestion: str = None,
        tone: str = None,
        topic: str = None,
    ):
        self.assistant_type = assistant_type
        self.content = content
        self.create_time = create_time
        self.dataset_name = dataset_name
        self.language = language
        self.regenerate = regenerate
        self.reply = reply
        self.score = score
        self.source_uri = source_uri
        self.suggestion = suggestion
        self.tone = tone
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant_type is not None:
            result['AssistantType'] = self.assistant_type
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.language is not None:
            result['Language'] = self.language
        if self.regenerate is not None:
            result['Regenerate'] = self.regenerate
        if self.reply is not None:
            result['Reply'] = self.reply
        if self.score is not None:
            result['Score'] = self.score
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.tone is not None:
            result['Tone'] = self.tone
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssistantType') is not None:
            self.assistant_type = m.get('AssistantType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Regenerate') is not None:
            self.regenerate = m.get('Regenerate')
        if m.get('Reply') is not None:
            self.reply = m.get('Reply')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Tone') is not None:
            self.tone = m.get('Tone')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class Notification(TeaModel):
    def __init__(
        self,
        extended_message_uri: str = None,
        mns: MNS = None,
        rocket_mq: RocketMQ = None,
    ):
        self.extended_message_uri = extended_message_uri
        self.mns = mns
        self.rocket_mq = rocket_mq

    def validate(self):
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_message_uri is not None:
            result['ExtendedMessageURI'] = self.extended_message_uri
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedMessageURI') is not None:
            self.extended_message_uri = m.get('ExtendedMessageURI')
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        if m.get('RocketMQ') is not None:
            temp_model = RocketMQ()
            self.rocket_mq = temp_model.from_map(m['RocketMQ'])
        return self


class OctreeOption(TeaModel):
    def __init__(
        self,
        do_voxel_grid_down_down_sampling: bool = None,
        library_name: str = None,
        octree_resolution: float = None,
        point_resolution: float = None,
    ):
        self.do_voxel_grid_down_down_sampling = do_voxel_grid_down_down_sampling
        self.library_name = library_name
        self.octree_resolution = octree_resolution
        self.point_resolution = point_resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.do_voxel_grid_down_down_sampling is not None:
            result['DoVoxelGridDownDownSampling'] = self.do_voxel_grid_down_down_sampling
        if self.library_name is not None:
            result['LibraryName'] = self.library_name
        if self.octree_resolution is not None:
            result['OctreeResolution'] = self.octree_resolution
        if self.point_resolution is not None:
            result['PointResolution'] = self.point_resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DoVoxelGridDownDownSampling') is not None:
            self.do_voxel_grid_down_down_sampling = m.get('DoVoxelGridDownDownSampling')
        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')
        if m.get('OctreeResolution') is not None:
            self.octree_resolution = m.get('OctreeResolution')
        if m.get('PointResolution') is not None:
            self.point_resolution = m.get('PointResolution')
        return self


class ProjectTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class Project(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_count: int = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        engine_concurrency: int = None,
        file_count: int = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        project_queries_per_second: int = None,
        service_role: str = None,
        tags: List[ProjectTags] = None,
        template_id: str = None,
        total_file_size: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.dataset_count = dataset_count
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.description = description
        self.engine_concurrency = engine_concurrency
        self.file_count = file_count
        self.project_max_dataset_count = project_max_dataset_count
        self.project_name = project_name
        self.project_queries_per_second = project_queries_per_second
        self.service_role = service_role
        self.tags = tags
        self.template_id = template_id
        self.total_file_size = total_file_size
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_count is not None:
            result['DatasetCount'] = self.dataset_count
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.engine_concurrency is not None:
            result['EngineConcurrency'] = self.engine_concurrency
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_queries_per_second is not None:
            result['ProjectQueriesPerSecond'] = self.project_queries_per_second
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetCount') is not None:
            self.dataset_count = m.get('DatasetCount')
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EngineConcurrency') is not None:
            self.engine_concurrency = m.get('EngineConcurrency')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQueriesPerSecond') is not None:
            self.project_queries_per_second = m.get('ProjectQueriesPerSecond')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ProjectTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class RegionType(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class Row(TeaModel):
    def __init__(
        self,
        custom_labels: List[KeyValuePair] = None,
        uri: str = None,
    ):
        self.custom_labels = custom_labels
        self.uri = uri

    def validate(self):
        if self.custom_labels:
            for k in self.custom_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomLabels'] = []
        if self.custom_labels is not None:
            for k in self.custom_labels:
                result['CustomLabels'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_labels = []
        if m.get('CustomLabels') is not None:
            for k in m.get('CustomLabels'):
                temp_model = KeyValuePair()
                self.custom_labels.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class SimilarImage(TeaModel):
    def __init__(
        self,
        image_score: float = None,
        uri: str = None,
    ):
        self.image_score = image_score
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_score is not None:
            result['ImageScore'] = self.image_score
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            self.image_score = m.get('ImageScore')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class SimilarImageCluster(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        custom_labels: Dict[str, Any] = None,
        files: List[SimilarImage] = None,
        object_id: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.custom_labels = custom_labels
        self.files = files
        self.object_id = object_id
        self.update_time = update_time

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = SimilarImage()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class SimpleQuery(TeaModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
        sub_queries: List['SimpleQuery'] = None,
        value: str = None,
    ):
        self.field = field
        self.operation = operation
        self.sub_queries = sub_queries
        self.value = value

    def validate(self):
        if self.sub_queries:
            for k in self.sub_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        result['SubQueries'] = []
        if self.sub_queries is not None:
            for k in self.sub_queries:
                result['SubQueries'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        self.sub_queries = []
        if m.get('SubQueries') is not None:
            for k in m.get('SubQueries'):
                temp_model = SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Story(TeaModel):
    def __init__(
        self,
        addresses: List[Address] = None,
        cover: File = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        figure_cluster_ids: List[str] = None,
        files: List[File] = None,
        object_id: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        update_time: str = None,
    ):
        self.addresses = addresses
        self.cover = cover
        self.create_time = create_time
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.figure_cluster_ids = figure_cluster_ids
        self.files = files
        self.object_id = object_id
        self.object_type = object_type
        self.owner_id = owner_id
        self.project_name = project_name
        self.story_end_time = story_end_time
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.update_time = update_time

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Cover') is not None:
            temp_model = File()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class TargetAudioFilterAudio(TeaModel):
    def __init__(
        self,
        mixing: bool = None,
    ):
        self.mixing = mixing

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mixing is not None:
            result['Mixing'] = self.mixing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mixing') is not None:
            self.mixing = m.get('Mixing')
        return self


class TargetAudioTranscodeAudio(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        bitrate_option: str = None,
        bits_per_sample: int = None,
        channel: int = None,
        codec: str = None,
        quality: int = None,
        sample_rate: int = None,
        sample_rate_option: str = None,
    ):
        self.bitrate = bitrate
        self.bitrate_option = bitrate_option
        self.bits_per_sample = bits_per_sample
        self.channel = channel
        self.codec = codec
        self.quality = quality
        self.sample_rate = sample_rate
        self.sample_rate_option = sample_rate_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option
        if self.bits_per_sample is not None:
            result['BitsPerSample'] = self.bits_per_sample
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.sample_rate_option is not None:
            result['SampleRateOption'] = self.sample_rate_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')
        if m.get('BitsPerSample') is not None:
            self.bits_per_sample = m.get('BitsPerSample')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SampleRateOption') is not None:
            self.sample_rate_option = m.get('SampleRateOption')
        return self


class TargetAudio(TeaModel):
    def __init__(
        self,
        disable_audio: bool = None,
        filter_audio: TargetAudioFilterAudio = None,
        stream: List[int] = None,
        transcode_audio: TargetAudioTranscodeAudio = None,
    ):
        self.disable_audio = disable_audio
        self.filter_audio = filter_audio
        self.stream = stream
        self.transcode_audio = transcode_audio

    def validate(self):
        if self.filter_audio:
            self.filter_audio.validate()
        if self.transcode_audio:
            self.transcode_audio.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_audio is not None:
            result['DisableAudio'] = self.disable_audio
        if self.filter_audio is not None:
            result['FilterAudio'] = self.filter_audio.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.transcode_audio is not None:
            result['TranscodeAudio'] = self.transcode_audio.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableAudio') is not None:
            self.disable_audio = m.get('DisableAudio')
        if m.get('FilterAudio') is not None:
            temp_model = TargetAudioFilterAudio()
            self.filter_audio = temp_model.from_map(m['FilterAudio'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('TranscodeAudio') is not None:
            temp_model = TargetAudioTranscodeAudio()
            self.transcode_audio = temp_model.from_map(m['TranscodeAudio'])
        return self


class TargetImageAnimations(TeaModel):
    def __init__(
        self,
        format: str = None,
        frame_rate: float = None,
        height: float = None,
        interval: float = None,
        number: int = None,
        scale_type: str = None,
        start_time: float = None,
        uri: str = None,
        width: float = None,
    ):
        # This parameter is required.
        self.format = format
        self.frame_rate = frame_rate
        self.height = height
        self.interval = interval
        self.number = number
        self.scale_type = scale_type
        self.start_time = start_time
        # This parameter is required.
        self.uri = uri
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.height is not None:
            result['Height'] = self.height
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.number is not None:
            result['Number'] = self.number
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetImageSnapshots(TeaModel):
    def __init__(
        self,
        format: str = None,
        height: float = None,
        interval: float = None,
        number: int = None,
        scale_type: str = None,
        start_time: float = None,
        uri: str = None,
        width: float = None,
    ):
        # This parameter is required.
        self.format = format
        self.height = height
        self.interval = interval
        self.number = number
        self.scale_type = scale_type
        self.start_time = start_time
        # This parameter is required.
        self.uri = uri
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.height is not None:
            result['Height'] = self.height
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.number is not None:
            result['Number'] = self.number
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetImageSprites(TeaModel):
    def __init__(
        self,
        format: str = None,
        interval: float = None,
        margin: int = None,
        number: int = None,
        pad: int = None,
        scale_height: float = None,
        scale_type: str = None,
        scale_width: float = None,
        start_time: float = None,
        tile_height: int = None,
        tile_width: int = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.format = format
        self.interval = interval
        self.margin = margin
        self.number = number
        self.pad = pad
        self.scale_height = scale_height
        self.scale_type = scale_type
        self.scale_width = scale_width
        self.start_time = start_time
        self.tile_height = tile_height
        self.tile_width = tile_width
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.number is not None:
            result['Number'] = self.number
        if self.pad is not None:
            result['Pad'] = self.pad
        if self.scale_height is not None:
            result['ScaleHeight'] = self.scale_height
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.scale_width is not None:
            result['ScaleWidth'] = self.scale_width
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tile_height is not None:
            result['TileHeight'] = self.tile_height
        if self.tile_width is not None:
            result['TileWidth'] = self.tile_width
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pad') is not None:
            self.pad = m.get('Pad')
        if m.get('ScaleHeight') is not None:
            self.scale_height = m.get('ScaleHeight')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('ScaleWidth') is not None:
            self.scale_width = m.get('ScaleWidth')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TileHeight') is not None:
            self.tile_height = m.get('TileHeight')
        if m.get('TileWidth') is not None:
            self.tile_width = m.get('TileWidth')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class TargetImage(TeaModel):
    def __init__(
        self,
        animations: List[TargetImageAnimations] = None,
        snapshots: List[TargetImageSnapshots] = None,
        sprites: List[TargetImageSprites] = None,
    ):
        self.animations = animations
        self.snapshots = snapshots
        self.sprites = sprites

    def validate(self):
        if self.animations:
            for k in self.animations:
                if k:
                    k.validate()
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()
        if self.sprites:
            for k in self.sprites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Animations'] = []
        if self.animations is not None:
            for k in self.animations:
                result['Animations'].append(k.to_map() if k else None)
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        result['Sprites'] = []
        if self.sprites is not None:
            for k in self.sprites:
                result['Sprites'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.animations = []
        if m.get('Animations') is not None:
            for k in m.get('Animations'):
                temp_model = TargetImageAnimations()
                self.animations.append(temp_model.from_map(k))
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = TargetImageSnapshots()
                self.snapshots.append(temp_model.from_map(k))
        self.sprites = []
        if m.get('Sprites') is not None:
            for k in m.get('Sprites'):
                temp_model = TargetImageSprites()
                self.sprites.append(temp_model.from_map(k))
        return self


class TargetSubtitleExtractSubtitle(TeaModel):
    def __init__(
        self,
        format: str = None,
        uri: str = None,
    ):
        self.format = format
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class TargetSubtitle(TeaModel):
    def __init__(
        self,
        disable_subtitle: bool = None,
        extract_subtitle: TargetSubtitleExtractSubtitle = None,
        stream: List[int] = None,
    ):
        self.disable_subtitle = disable_subtitle
        self.extract_subtitle = extract_subtitle
        self.stream = stream

    def validate(self):
        if self.extract_subtitle:
            self.extract_subtitle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_subtitle is not None:
            result['DisableSubtitle'] = self.disable_subtitle
        if self.extract_subtitle is not None:
            result['ExtractSubtitle'] = self.extract_subtitle.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableSubtitle') is not None:
            self.disable_subtitle = m.get('DisableSubtitle')
        if m.get('ExtractSubtitle') is not None:
            temp_model = TargetSubtitleExtractSubtitle()
            self.extract_subtitle = temp_model.from_map(m['ExtractSubtitle'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class TargetVideoFilterVideoDelogos(TeaModel):
    def __init__(
        self,
        duration: float = None,
        dx: float = None,
        dy: float = None,
        height: float = None,
        refer_pos: str = None,
        start_time: float = None,
        width: float = None,
    ):
        self.duration = duration
        self.dx = dx
        self.dy = dy
        self.height = height
        self.refer_pos = refer_pos
        self.start_time = start_time
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dx is not None:
            result['Dx'] = self.dx
        if self.dy is not None:
            result['Dy'] = self.dy
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')
        if m.get('Dy') is not None:
            self.dy = m.get('Dy')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetVideoFilterVideoWatermarks(TeaModel):
    def __init__(
        self,
        border_color: str = None,
        border_width: int = None,
        content: str = None,
        duration: float = None,
        dx: float = None,
        dy: float = None,
        font_apha: float = None,
        font_color: str = None,
        font_name: str = None,
        font_size: int = None,
        height: float = None,
        refer_pos: str = None,
        start_time: float = None,
        type: str = None,
        uri: str = None,
        width: float = None,
    ):
        self.border_color = border_color
        self.border_width = border_width
        self.content = content
        self.duration = duration
        self.dx = dx
        self.dy = dy
        self.font_apha = font_apha
        self.font_color = font_color
        self.font_name = font_name
        self.font_size = font_size
        self.height = height
        self.refer_pos = refer_pos
        self.start_time = start_time
        self.type = type
        self.uri = uri
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.content is not None:
            result['Content'] = self.content
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dx is not None:
            result['Dx'] = self.dx
        if self.dy is not None:
            result['Dy'] = self.dy
        if self.font_apha is not None:
            result['FontApha'] = self.font_apha
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')
        if m.get('Dy') is not None:
            self.dy = m.get('Dy')
        if m.get('FontApha') is not None:
            self.font_apha = m.get('FontApha')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetVideoFilterVideo(TeaModel):
    def __init__(
        self,
        delogos: List[TargetVideoFilterVideoDelogos] = None,
        watermarks: List[TargetVideoFilterVideoWatermarks] = None,
    ):
        self.delogos = delogos
        self.watermarks = watermarks

    def validate(self):
        if self.delogos:
            for k in self.delogos:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delogos'] = []
        if self.delogos is not None:
            for k in self.delogos:
                result['Delogos'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delogos = []
        if m.get('Delogos') is not None:
            for k in m.get('Delogos'):
                temp_model = TargetVideoFilterVideoDelogos()
                self.delogos.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = TargetVideoFilterVideoWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class TargetVideoTranscodeVideo(TeaModel):
    def __init__(
        self,
        adaptive_resolution_direction: bool = None,
        bframes: int = None,
        bitrate: int = None,
        bitrate_option: str = None,
        buffer_size: int = None,
        crf: float = None,
        codec: str = None,
        frame_rate: float = None,
        frame_rate_option: str = None,
        gopsize: int = None,
        max_bitrate: int = None,
        pixel_format: str = None,
        refs: int = None,
        resolution: str = None,
        resolution_option: str = None,
        rotation: int = None,
        scale_type: str = None,
    ):
        self.adaptive_resolution_direction = adaptive_resolution_direction
        self.bframes = bframes
        self.bitrate = bitrate
        self.bitrate_option = bitrate_option
        self.buffer_size = buffer_size
        self.crf = crf
        self.codec = codec
        self.frame_rate = frame_rate
        self.frame_rate_option = frame_rate_option
        self.gopsize = gopsize
        self.max_bitrate = max_bitrate
        self.pixel_format = pixel_format
        self.refs = refs
        self.resolution = resolution
        self.resolution_option = resolution_option
        self.rotation = rotation
        self.scale_type = scale_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adaptive_resolution_direction is not None:
            result['AdaptiveResolutionDirection'] = self.adaptive_resolution_direction
        if self.bframes is not None:
            result['BFrames'] = self.bframes
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option
        if self.buffer_size is not None:
            result['BufferSize'] = self.buffer_size
        if self.crf is not None:
            result['CRF'] = self.crf
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.frame_rate_option is not None:
            result['FrameRateOption'] = self.frame_rate_option
        if self.gopsize is not None:
            result['GOPSize'] = self.gopsize
        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.refs is not None:
            result['Refs'] = self.refs
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.resolution_option is not None:
            result['ResolutionOption'] = self.resolution_option
        if self.rotation is not None:
            result['Rotation'] = self.rotation
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptiveResolutionDirection') is not None:
            self.adaptive_resolution_direction = m.get('AdaptiveResolutionDirection')
        if m.get('BFrames') is not None:
            self.bframes = m.get('BFrames')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')
        if m.get('BufferSize') is not None:
            self.buffer_size = m.get('BufferSize')
        if m.get('CRF') is not None:
            self.crf = m.get('CRF')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('FrameRateOption') is not None:
            self.frame_rate_option = m.get('FrameRateOption')
        if m.get('GOPSize') is not None:
            self.gopsize = m.get('GOPSize')
        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Refs') is not None:
            self.refs = m.get('Refs')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ResolutionOption') is not None:
            self.resolution_option = m.get('ResolutionOption')
        if m.get('Rotation') is not None:
            self.rotation = m.get('Rotation')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        return self


class TargetVideo(TeaModel):
    def __init__(
        self,
        disable_video: bool = None,
        filter_video: TargetVideoFilterVideo = None,
        stream: List[int] = None,
        transcode_video: TargetVideoTranscodeVideo = None,
    ):
        self.disable_video = disable_video
        self.filter_video = filter_video
        self.stream = stream
        self.transcode_video = transcode_video

    def validate(self):
        if self.filter_video:
            self.filter_video.validate()
        if self.transcode_video:
            self.transcode_video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_video is not None:
            result['DisableVideo'] = self.disable_video
        if self.filter_video is not None:
            result['FilterVideo'] = self.filter_video.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.transcode_video is not None:
            result['TranscodeVideo'] = self.transcode_video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableVideo') is not None:
            self.disable_video = m.get('DisableVideo')
        if m.get('FilterVideo') is not None:
            temp_model = TargetVideoFilterVideo()
            self.filter_video = temp_model.from_map(m['FilterVideo'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('TranscodeVideo') is not None:
            temp_model = TargetVideoTranscodeVideo()
            self.transcode_video = temp_model.from_map(m['TranscodeVideo'])
        return self


class TaskInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        message: str = None,
        progress: int = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        task_id: str = None,
        task_request_definition: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.end_time = end_time
        self.message = message
        self.progress = progress
        self.start_time = start_time
        self.status = status
        self.tags = tags
        self.task_id = task_id
        self.task_request_definition = task_request_definition
        self.task_type = task_type
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_request_definition is not None:
            result['TaskRequestDefinition'] = self.task_request_definition
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskRequestDefinition') is not None:
            self.task_request_definition = m.get('TaskRequestDefinition')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class TimeRange(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class TrimPolicy(TeaModel):
    def __init__(
        self,
        disable_delete_empty_cell: bool = None,
        disable_delete_repeated_style: bool = None,
        disable_delete_unused_picture: bool = None,
        disable_delete_unused_shape: bool = None,
    ):
        self.disable_delete_empty_cell = disable_delete_empty_cell
        self.disable_delete_repeated_style = disable_delete_repeated_style
        self.disable_delete_unused_picture = disable_delete_unused_picture
        self.disable_delete_unused_shape = disable_delete_unused_shape

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_delete_empty_cell is not None:
            result['DisableDeleteEmptyCell'] = self.disable_delete_empty_cell
        if self.disable_delete_repeated_style is not None:
            result['DisableDeleteRepeatedStyle'] = self.disable_delete_repeated_style
        if self.disable_delete_unused_picture is not None:
            result['DisableDeleteUnusedPicture'] = self.disable_delete_unused_picture
        if self.disable_delete_unused_shape is not None:
            result['DisableDeleteUnusedShape'] = self.disable_delete_unused_shape
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableDeleteEmptyCell') is not None:
            self.disable_delete_empty_cell = m.get('DisableDeleteEmptyCell')
        if m.get('DisableDeleteRepeatedStyle') is not None:
            self.disable_delete_repeated_style = m.get('DisableDeleteRepeatedStyle')
        if m.get('DisableDeleteUnusedPicture') is not None:
            self.disable_delete_unused_picture = m.get('DisableDeleteUnusedPicture')
        if m.get('DisableDeleteUnusedShape') is not None:
            self.disable_delete_unused_shape = m.get('DisableDeleteUnusedShape')
        return self


class WebofficePermission(TeaModel):
    def __init__(
        self,
        copy: bool = None,
        export: bool = None,
        history: bool = None,
        print: bool = None,
        readonly: bool = None,
        rename: bool = None,
    ):
        self.copy = copy
        self.export = export
        self.history = history
        self.print = print
        self.readonly = readonly
        self.rename = rename

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy is not None:
            result['Copy'] = self.copy
        if self.export is not None:
            result['Export'] = self.export
        if self.history is not None:
            result['History'] = self.history
        if self.print is not None:
            result['Print'] = self.print
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        if self.rename is not None:
            result['Rename'] = self.rename
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Copy') is not None:
            self.copy = m.get('Copy')
        if m.get('Export') is not None:
            self.export = m.get('Export')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Print') is not None:
            self.print = m.get('Print')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        if m.get('Rename') is not None:
            self.rename = m.get('Rename')
        return self


class WebofficeUser(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        id: str = None,
        name: str = None,
    ):
        self.avatar = avatar
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class WebofficeWatermark(TeaModel):
    def __init__(
        self,
        fill_style: str = None,
        font: str = None,
        horizontal: int = None,
        rotate: float = None,
        type: int = None,
        value: str = None,
        vertical: int = None,
    ):
        self.fill_style = fill_style
        self.font = font
        self.horizontal = horizontal
        self.rotate = rotate
        self.type = type
        self.value = value
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fill_style is not None:
            result['FillStyle'] = self.fill_style
        if self.font is not None:
            result['Font'] = self.font
        if self.horizontal is not None:
            result['Horizontal'] = self.horizontal
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FillStyle') is not None:
            self.fill_style = m.get('FillStyle')
        if m.get('Font') is not None:
            self.font = m.get('Font')
        if m.get('Horizontal') is not None:
            self.horizontal = m.get('Horizontal')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        return self


class AddImageMosaicRequestTargetsBoundary(TeaModel):
    def __init__(
        self,
        height: float = None,
        refer_pos: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # This parameter is required.
        self.height = height
        self.refer_pos = refer_pos
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class AddImageMosaicRequestTargets(TeaModel):
    def __init__(
        self,
        blur_radius: int = None,
        boundary: AddImageMosaicRequestTargetsBoundary = None,
        color: str = None,
        mosaic_radius: int = None,
        sigma: int = None,
        type: str = None,
    ):
        self.blur_radius = blur_radius
        # This parameter is required.
        self.boundary = boundary
        self.color = color
        self.mosaic_radius = mosaic_radius
        self.sigma = sigma
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur_radius is not None:
            result['BlurRadius'] = self.blur_radius
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.color is not None:
            result['Color'] = self.color
        if self.mosaic_radius is not None:
            result['MosaicRadius'] = self.mosaic_radius
        if self.sigma is not None:
            result['Sigma'] = self.sigma
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlurRadius') is not None:
            self.blur_radius = m.get('BlurRadius')
        if m.get('Boundary') is not None:
            temp_model = AddImageMosaicRequestTargetsBoundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('MosaicRadius') is not None:
            self.mosaic_radius = m.get('MosaicRadius')
        if m.get('Sigma') is not None:
            self.sigma = m.get('Sigma')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddImageMosaicRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        image_format: str = None,
        project_name: str = None,
        quality: int = None,
        source_uri: str = None,
        target_uri: str = None,
        targets: List[AddImageMosaicRequestTargets] = None,
    ):
        self.credential_config = credential_config
        self.image_format = image_format
        # This parameter is required.
        self.project_name = project_name
        self.quality = quality
        # This parameter is required.
        self.source_uri = source_uri
        # This parameter is required.
        self.target_uri = target_uri
        # This parameter is required.
        self.targets = targets

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = AddImageMosaicRequestTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class AddImageMosaicShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        image_format: str = None,
        project_name: str = None,
        quality: int = None,
        source_uri: str = None,
        target_uri: str = None,
        targets_shrink: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.image_format = image_format
        # This parameter is required.
        self.project_name = project_name
        self.quality = quality
        # This parameter is required.
        self.source_uri = source_uri
        # This parameter is required.
        self.target_uri = target_uri
        # This parameter is required.
        self.targets_shrink = targets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        return self


class AddImageMosaicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddImageMosaicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageMosaicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddImageMosaicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddStoryFilesRequestFiles(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class AddStoryFilesRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[AddStoryFilesRequestFiles] = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files = files
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = AddStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AddStoryFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files_shrink = files_shrink
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AddStoryFilesResponseBodyFiles(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        uri: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class AddStoryFilesResponseBody(TeaModel):
    def __init__(
        self,
        files: List[AddStoryFilesResponseBodyFiles] = None,
        request_id: str = None,
    ):
        self.files = files
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = AddStoryFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddStoryFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddStoryFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachOSSBucketRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        ossbucket: str = None,
        project_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.ossbucket = ossbucket
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AttachOSSBucketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachOSSBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachOSSBucketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachOSSBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris: List[str] = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uris = uris

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchDeleteFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris_shrink: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uris_shrink = uris_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchDeleteFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetFigureClusterRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_ids: List[str] = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_ids = object_ids
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_ids is not None:
            result['ObjectIds'] = self.object_ids
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectIds') is not None:
            self.object_ids = m.get('ObjectIds')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchGetFigureClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_ids_shrink: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_ids_shrink is not None:
            result['ObjectIds'] = self.object_ids_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectIds') is not None:
            self.object_ids_shrink = m.get('ObjectIds')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchGetFigureClusterResponseBody(TeaModel):
    def __init__(
        self,
        figure_clusters: List[FigureCluster] = None,
        request_id: str = None,
    ):
        self.figure_clusters = figure_clusters
        self.request_id = request_id

    def validate(self):
        if self.figure_clusters:
            for k in self.figure_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FigureClusters'] = []
        if self.figure_clusters is not None:
            for k in self.figure_clusters:
                result['FigureClusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figure_clusters = []
        if m.get('FigureClusters') is not None:
            for k in m.get('FigureClusters'):
                temp_model = FigureCluster()
                self.figure_clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetFigureClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetFigureClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchGetFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris: List[str] = None,
        with_fields: List[str] = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uris = uris
        self.with_fields = with_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class BatchGetFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris_shrink: str = None,
        with_fields_shrink: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uris_shrink = uris_shrink
        self.with_fields_shrink = with_fields_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class BatchGetFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        request_id: str = None,
    ):
        self.files = files
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchGetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchIndexFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[InputFile] = None,
        notification: Notification = None,
        project_name: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files = files
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.user_data = user_data

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = InputFile()
                self.files.append(temp_model.from_map(k))
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class BatchIndexFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files_shrink = files_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class BatchIndexFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchIndexFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchIndexFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchIndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[InputFile] = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files = files
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = InputFile()
                self.files.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchUpdateFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files_shrink = files_shrink
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchUpdateFileMetaResponseBodyFiles(TeaModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
        uri: str = None,
    ):
        self.message = message
        self.success = success
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class BatchUpdateFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        files: List[BatchUpdateFileMetaResponseBodyFiles] = None,
        request_id: str = None,
    ):
        self.files = files
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = BatchUpdateFileMetaResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchUpdateFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareImageFacesRequestSource(TeaModel):
    def __init__(
        self,
        uri1: str = None,
        uri2: str = None,
    ):
        self.uri1 = uri1
        self.uri2 = uri2

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri1 is not None:
            result['URI1'] = self.uri1
        if self.uri2 is not None:
            result['URI2'] = self.uri2
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI1') is not None:
            self.uri1 = m.get('URI1')
        if m.get('URI2') is not None:
            self.uri2 = m.get('URI2')
        return self


class CompareImageFacesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source: CompareImageFacesRequestSource = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        self.source = source

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source is not None:
            result['Source'] = self.source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Source') is not None:
            temp_model = CompareImageFacesRequestSource()
            self.source = temp_model.from_map(m['Source'])
        return self


class CompareImageFacesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_shrink: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        self.source_shrink = source_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        return self


class CompareImageFacesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        similarity: float = None,
    ):
        self.request_id = request_id
        self.similarity = similarity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        return self


class CompareImageFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompareImageFacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CompareImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArchiveFileInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        notification: Notification = None,
        password: str = None,
        project_name: str = None,
        source_uri: str = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.notification = notification
        self.password = password
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateArchiveFileInspectionTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        password: str = None,
        project_name: str = None,
        source_uri: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.notification_shrink = notification_shrink
        self.password = password
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateArchiveFileInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateArchiveFileInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateArchiveFileInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateArchiveFileInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchRequestActions(TeaModel):
    def __init__(
        self,
        fast_fail_policy: FastFailPolicy = None,
        name: str = None,
        parameters: List[str] = None,
    ):
        self.fast_fail_policy = fast_fail_policy
        # This parameter is required.
        self.name = name
        self.parameters = parameters

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m['FastFailPolicy'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class CreateBatchRequestNotification(TeaModel):
    def __init__(
        self,
        mns: MNS = None,
    ):
        self.mns = mns

    def validate(self):
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        return self


class CreateBatchRequest(TeaModel):
    def __init__(
        self,
        actions: List[CreateBatchRequestActions] = None,
        input: Input = None,
        notification: CreateBatchRequestNotification = None,
        project_name: str = None,
        service_role: str = None,
        tags: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.actions = actions
        # This parameter is required.
        self.input = input
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.service_role = service_role
        self.tags = tags

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = CreateBatchRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Notification') is not None:
            temp_model = CreateBatchRequestNotification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateBatchShrinkRequest(TeaModel):
    def __init__(
        self,
        actions_shrink: str = None,
        input_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        service_role: str = None,
        tags_shrink: str = None,
    ):
        # This parameter is required.
        self.actions_shrink = actions_shrink
        # This parameter is required.
        self.input_shrink = input_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.service_role = service_role
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateBatchResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateBindingResponseBody(TeaModel):
    def __init__(
        self,
        binding: Binding = None,
        request_id: str = None,
    ):
        self.binding = binding
        self.request_id = request_id

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = Binding()
            self.binding = temp_model.from_map(m['Binding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCompressPointCloudTaskRequest(TeaModel):
    def __init__(
        self,
        compress_method: str = None,
        credential_config: CredentialConfig = None,
        kdtree_option: KdtreeOption = None,
        notification: Notification = None,
        octree_option: OctreeOption = None,
        point_cloud_fields: List[str] = None,
        point_cloud_file_format: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.compress_method = compress_method
        self.credential_config = credential_config
        self.kdtree_option = kdtree_option
        self.notification = notification
        self.octree_option = octree_option
        # This parameter is required.
        self.point_cloud_fields = point_cloud_fields
        self.point_cloud_file_format = point_cloud_file_format
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.tags = tags
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.kdtree_option:
            self.kdtree_option.validate()
        if self.notification:
            self.notification.validate()
        if self.octree_option:
            self.octree_option.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_method is not None:
            result['CompressMethod'] = self.compress_method
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.kdtree_option is not None:
            result['KdtreeOption'] = self.kdtree_option.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.octree_option is not None:
            result['OctreeOption'] = self.octree_option.to_map()
        if self.point_cloud_fields is not None:
            result['PointCloudFields'] = self.point_cloud_fields
        if self.point_cloud_file_format is not None:
            result['PointCloudFileFormat'] = self.point_cloud_file_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressMethod') is not None:
            self.compress_method = m.get('CompressMethod')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('KdtreeOption') is not None:
            temp_model = KdtreeOption()
            self.kdtree_option = temp_model.from_map(m['KdtreeOption'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('OctreeOption') is not None:
            temp_model = OctreeOption()
            self.octree_option = temp_model.from_map(m['OctreeOption'])
        if m.get('PointCloudFields') is not None:
            self.point_cloud_fields = m.get('PointCloudFields')
        if m.get('PointCloudFileFormat') is not None:
            self.point_cloud_file_format = m.get('PointCloudFileFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateCompressPointCloudTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        compress_method: str = None,
        credential_config_shrink: str = None,
        kdtree_option_shrink: str = None,
        notification_shrink: str = None,
        octree_option_shrink: str = None,
        point_cloud_fields_shrink: str = None,
        point_cloud_file_format: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.compress_method = compress_method
        self.credential_config_shrink = credential_config_shrink
        self.kdtree_option_shrink = kdtree_option_shrink
        self.notification_shrink = notification_shrink
        self.octree_option_shrink = octree_option_shrink
        # This parameter is required.
        self.point_cloud_fields_shrink = point_cloud_fields_shrink
        self.point_cloud_file_format = point_cloud_file_format
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_method is not None:
            result['CompressMethod'] = self.compress_method
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.kdtree_option_shrink is not None:
            result['KdtreeOption'] = self.kdtree_option_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.octree_option_shrink is not None:
            result['OctreeOption'] = self.octree_option_shrink
        if self.point_cloud_fields_shrink is not None:
            result['PointCloudFields'] = self.point_cloud_fields_shrink
        if self.point_cloud_file_format is not None:
            result['PointCloudFileFormat'] = self.point_cloud_file_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressMethod') is not None:
            self.compress_method = m.get('CompressMethod')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('KdtreeOption') is not None:
            self.kdtree_option_shrink = m.get('KdtreeOption')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('OctreeOption') is not None:
            self.octree_option_shrink = m.get('OctreeOption')
        if m.get('PointCloudFields') is not None:
            self.point_cloud_fields_shrink = m.get('PointCloudFields')
        if m.get('PointCloudFileFormat') is not None:
            self.point_cloud_file_format = m.get('PointCloudFileFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateCompressPointCloudTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateCompressPointCloudTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCompressPointCloudTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCompressPointCloudTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedStoryRequestCover(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateCustomizedStoryRequestFiles(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateCustomizedStoryRequest(TeaModel):
    def __init__(
        self,
        cover: CreateCustomizedStoryRequestCover = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        files: List[CreateCustomizedStoryRequestFiles] = None,
        project_name: str = None,
        story_name: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        # This parameter is required.
        self.cover = cover
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files = files
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.story_name = story_name
        # This parameter is required.
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        if self.cover:
            self.cover.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = CreateCustomizedStoryRequestCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = CreateCustomizedStoryRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        return self


class CreateCustomizedStoryShrinkRequest(TeaModel):
    def __init__(
        self,
        cover_shrink: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        files_shrink: str = None,
        project_name: str = None,
        story_name: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        # This parameter is required.
        self.cover_shrink = cover_shrink
        self.custom_labels_shrink = custom_labels_shrink
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files_shrink = files_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.story_name = story_name
        # This parameter is required.
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        return self


class CreateCustomizedStoryResponseBody(TeaModel):
    def __init__(
        self,
        object_id: str = None,
        request_id: str = None,
    ):
        self.object_id = object_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomizedStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomizedStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomizedStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        project_name: str = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # This parameter is required.
        self.dataset_name = dataset_name
        self.description = description
        # This parameter is required.
        self.project_name = project_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset: Dataset = None,
        request_id: str = None,
    ):
        self.dataset = dataset
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDecodeBlindWatermarkTaskRequest(TeaModel):
    def __init__(
        self,
        image_quality: int = None,
        model: str = None,
        notification: Notification = None,
        original_image_uri: str = None,
        project_name: str = None,
        source_uri: str = None,
        strength_level: str = None,
        target_uri: str = None,
        watermark_type: str = None,
    ):
        self.image_quality = image_quality
        self.model = model
        self.notification = notification
        self.original_image_uri = original_image_uri
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.strength_level = strength_level
        self.target_uri = target_uri
        self.watermark_type = watermark_type

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.model is not None:
            result['Model'] = self.model
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.original_image_uri is not None:
            result['OriginalImageURI'] = self.original_image_uri
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.strength_level is not None:
            result['StrengthLevel'] = self.strength_level
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('OriginalImageURI') is not None:
            self.original_image_uri = m.get('OriginalImageURI')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StrengthLevel') is not None:
            self.strength_level = m.get('StrengthLevel')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class CreateDecodeBlindWatermarkTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        image_quality: int = None,
        model: str = None,
        notification_shrink: str = None,
        original_image_uri: str = None,
        project_name: str = None,
        source_uri: str = None,
        strength_level: str = None,
        target_uri: str = None,
        watermark_type: str = None,
    ):
        self.image_quality = image_quality
        self.model = model
        self.notification_shrink = notification_shrink
        self.original_image_uri = original_image_uri
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.strength_level = strength_level
        self.target_uri = target_uri
        self.watermark_type = watermark_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.model is not None:
            result['Model'] = self.model
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.original_image_uri is not None:
            result['OriginalImageURI'] = self.original_image_uri
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.strength_level is not None:
            result['StrengthLevel'] = self.strength_level
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('OriginalImageURI') is not None:
            self.original_image_uri = m.get('OriginalImageURI')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StrengthLevel') is not None:
            self.strength_level = m.get('StrengthLevel')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class CreateDecodeBlindWatermarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDecodeBlindWatermarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDecodeBlindWatermarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDecodeBlindWatermarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFacesSearchingTaskRequestSources(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateFacesSearchingTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_result: int = None,
        notification: Notification = None,
        project_name: str = None,
        sources: List[CreateFacesSearchingTaskRequestSources] = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_result = max_result
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.sources = sources
        self.user_data = user_data

    def validate(self):
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateFacesSearchingTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFacesSearchingTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_result: int = None,
        notification_shrink: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_result = max_result
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.sources_shrink = sources_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFacesSearchingTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFacesSearchingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFacesSearchingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFacesSearchingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFigureClusteringTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notification: Notification = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClusteringTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClusteringTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFigureClusteringTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFigureClusteringTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFigureClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFigureClustersMergingTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        from_: str = None,
        froms: List[str] = None,
        notification: Notification = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        to: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.from_ = from_
        self.froms = froms
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.tags = tags
        # This parameter is required.
        self.to = to
        self.user_data = user_data

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.from_ is not None:
            result['From'] = self.from_
        if self.froms is not None:
            result['Froms'] = self.froms
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.to is not None:
            result['To'] = self.to
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Froms') is not None:
            self.froms = m.get('Froms')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClustersMergingTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        from_: str = None,
        froms_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        to: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.from_ = from_
        self.froms_shrink = froms_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.to = to
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.from_ is not None:
            result['From'] = self.from_
        if self.froms_shrink is not None:
            result['Froms'] = self.froms_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Froms') is not None:
            self.froms_shrink = m.get('Froms')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClustersMergingTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFigureClustersMergingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFigureClustersMergingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFigureClustersMergingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileCompressionTaskRequestSources(TeaModel):
    def __init__(
        self,
        alias: str = None,
        mode: str = None,
        uri: str = None,
    ):
        self.alias = alias
        self.mode = mode
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateFileCompressionTaskRequest(TeaModel):
    def __init__(
        self,
        compressed_format: str = None,
        credential_config: CredentialConfig = None,
        notification: Notification = None,
        project_name: str = None,
        source_manifest_uri: str = None,
        sources: List[CreateFileCompressionTaskRequestSources] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.compressed_format = compressed_format
        self.credential_config = credential_config
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.source_manifest_uri = source_manifest_uri
        self.sources = sources
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed_format is not None:
            result['CompressedFormat'] = self.compressed_format
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_manifest_uri is not None:
            result['SourceManifestURI'] = self.source_manifest_uri
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressedFormat') is not None:
            self.compressed_format = m.get('CompressedFormat')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceManifestURI') is not None:
            self.source_manifest_uri = m.get('SourceManifestURI')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateFileCompressionTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileCompressionTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        compressed_format: str = None,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        source_manifest_uri: str = None,
        sources_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.compressed_format = compressed_format
        self.credential_config_shrink = credential_config_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.source_manifest_uri = source_manifest_uri
        self.sources_shrink = sources_shrink
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed_format is not None:
            result['CompressedFormat'] = self.compressed_format
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_manifest_uri is not None:
            result['SourceManifestURI'] = self.source_manifest_uri
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressedFormat') is not None:
            self.compressed_format = m.get('CompressedFormat')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceManifestURI') is not None:
            self.source_manifest_uri = m.get('SourceManifestURI')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileCompressionTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFileCompressionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileCompressionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFileCompressionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileUncompressionTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        notification: Notification = None,
        password: str = None,
        project_name: str = None,
        selected_files: List[str] = None,
        source_uri: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.notification = notification
        self.password = password
        # This parameter is required.
        self.project_name = project_name
        self.selected_files = selected_files
        # This parameter is required.
        self.source_uri = source_uri
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.selected_files is not None:
            result['SelectedFiles'] = self.selected_files
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SelectedFiles') is not None:
            self.selected_files = m.get('SelectedFiles')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileUncompressionTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        password: str = None,
        project_name: str = None,
        selected_files_shrink: str = None,
        source_uri: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.notification_shrink = notification_shrink
        self.password = password
        # This parameter is required.
        self.project_name = project_name
        self.selected_files_shrink = selected_files_shrink
        # This parameter is required.
        self.source_uri = source_uri
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.selected_files_shrink is not None:
            result['SelectedFiles'] = self.selected_files_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SelectedFiles') is not None:
            self.selected_files_shrink = m.get('SelectedFiles')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileUncompressionTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFileUncompressionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileUncompressionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFileUncompressionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageModerationTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        interval: int = None,
        max_frames: int = None,
        notification: Notification = None,
        project_name: str = None,
        scenes: List[str] = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.interval = interval
        self.max_frames = max_frames
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.scenes = scenes
        # This parameter is required.
        self.source_uri = source_uri
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes is not None:
            result['Scenes'] = self.scenes
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageModerationTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        interval: int = None,
        max_frames: int = None,
        notification_shrink: str = None,
        project_name: str = None,
        scenes_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.interval = interval
        self.max_frames = max_frames
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.scenes_shrink = scenes_shrink
        # This parameter is required.
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageModerationTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageModerationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageModerationTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateImageModerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageSplicingTaskRequestSources(TeaModel):
    def __init__(
        self,
        rotate: int = None,
        uri: str = None,
    ):
        self.rotate = rotate
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateImageSplicingTaskRequest(TeaModel):
    def __init__(
        self,
        align: int = None,
        background_color: str = None,
        credential_config: CredentialConfig = None,
        direction: str = None,
        image_format: str = None,
        margin: int = None,
        notification: Notification = None,
        padding: int = None,
        project_name: str = None,
        quality: int = None,
        scale_type: str = None,
        sources: List[CreateImageSplicingTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.align = align
        self.background_color = background_color
        self.credential_config = credential_config
        self.direction = direction
        self.image_format = image_format
        self.margin = margin
        self.notification = notification
        self.padding = padding
        # This parameter is required.
        self.project_name = project_name
        self.quality = quality
        self.scale_type = scale_type
        # This parameter is required.
        self.sources = sources
        self.tags = tags
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['Align'] = self.align
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.padding is not None:
            result['Padding'] = self.padding
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Padding') is not None:
            self.padding = m.get('Padding')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateImageSplicingTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageSplicingTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        align: int = None,
        background_color: str = None,
        credential_config_shrink: str = None,
        direction: str = None,
        image_format: str = None,
        margin: int = None,
        notification_shrink: str = None,
        padding: int = None,
        project_name: str = None,
        quality: int = None,
        scale_type: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.align = align
        self.background_color = background_color
        self.credential_config_shrink = credential_config_shrink
        self.direction = direction
        self.image_format = image_format
        self.margin = margin
        self.notification_shrink = notification_shrink
        self.padding = padding
        # This parameter is required.
        self.project_name = project_name
        self.quality = quality
        self.scale_type = scale_type
        # This parameter is required.
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['Align'] = self.align
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.padding is not None:
            result['Padding'] = self.padding
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Padding') is not None:
            self.padding = m.get('Padding')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageSplicingTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageSplicingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageSplicingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateImageSplicingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageToPDFTaskRequestSources(TeaModel):
    def __init__(
        self,
        rotate: int = None,
        uri: str = None,
    ):
        self.rotate = rotate
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateImageToPDFTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        notification: Notification = None,
        project_name: str = None,
        sources: List[CreateImageToPDFTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.sources = sources
        self.tags = tags
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateImageToPDFTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageToPDFTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageToPDFTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageToPDFTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageToPDFTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateImageToPDFTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocationDateClusteringTaskRequestDateOptions(TeaModel):
    def __init__(
        self,
        gap_days: int = None,
        max_days: int = None,
        min_days: int = None,
    ):
        # This parameter is required.
        self.gap_days = gap_days
        # This parameter is required.
        self.max_days = max_days
        # This parameter is required.
        self.min_days = min_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gap_days is not None:
            result['GapDays'] = self.gap_days
        if self.max_days is not None:
            result['MaxDays'] = self.max_days
        if self.min_days is not None:
            result['MinDays'] = self.min_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GapDays') is not None:
            self.gap_days = m.get('GapDays')
        if m.get('MaxDays') is not None:
            self.max_days = m.get('MaxDays')
        if m.get('MinDays') is not None:
            self.min_days = m.get('MinDays')
        return self


class CreateLocationDateClusteringTaskRequestLocationOptions(TeaModel):
    def __init__(
        self,
        location_date_cluster_levels: List[str] = None,
    ):
        # This parameter is required.
        self.location_date_cluster_levels = location_date_cluster_levels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_date_cluster_levels is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels = m.get('LocationDateClusterLevels')
        return self


class CreateLocationDateClusteringTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        date_options: CreateLocationDateClusteringTaskRequestDateOptions = None,
        location_options: CreateLocationDateClusteringTaskRequestLocationOptions = None,
        notification: Notification = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.date_options = date_options
        # This parameter is required.
        self.location_options = location_options
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.date_options:
            self.date_options.validate()
        if self.location_options:
            self.location_options.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.date_options is not None:
            result['DateOptions'] = self.date_options.to_map()
        if self.location_options is not None:
            result['LocationOptions'] = self.location_options.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('DateOptions') is not None:
            temp_model = CreateLocationDateClusteringTaskRequestDateOptions()
            self.date_options = temp_model.from_map(m['DateOptions'])
        if m.get('LocationOptions') is not None:
            temp_model = CreateLocationDateClusteringTaskRequestLocationOptions()
            self.location_options = temp_model.from_map(m['LocationOptions'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateLocationDateClusteringTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        date_options_shrink: str = None,
        location_options_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.date_options_shrink = date_options_shrink
        # This parameter is required.
        self.location_options_shrink = location_options_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.date_options_shrink is not None:
            result['DateOptions'] = self.date_options_shrink
        if self.location_options_shrink is not None:
            result['LocationOptions'] = self.location_options_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('DateOptions') is not None:
            self.date_options_shrink = m.get('DateOptions')
        if m.get('LocationOptions') is not None:
            self.location_options_shrink = m.get('LocationOptions')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateLocationDateClusteringTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateLocationDateClusteringTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLocationDateClusteringTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLocationDateClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMediaConvertTaskRequestSourcesSubtitles(TeaModel):
    def __init__(
        self,
        language: str = None,
        time_offset: float = None,
        uri: str = None,
    ):
        self.language = language
        self.time_offset = time_offset
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.time_offset is not None:
            result['TimeOffset'] = self.time_offset
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TimeOffset') is not None:
            self.time_offset = m.get('TimeOffset')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestSources(TeaModel):
    def __init__(
        self,
        duration: float = None,
        start_time: float = None,
        subtitles: List[CreateMediaConvertTaskRequestSourcesSubtitles] = None,
        uri: str = None,
    ):
        self.duration = duration
        self.start_time = start_time
        self.subtitles = subtitles
        self.uri = uri

    def validate(self):
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = CreateMediaConvertTaskRequestSourcesSubtitles()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestTargetsSegment(TeaModel):
    def __init__(
        self,
        duration: float = None,
        format: str = None,
        start_number: int = None,
    ):
        self.duration = duration
        self.format = format
        self.start_number = start_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format is not None:
            result['Format'] = self.format
        if self.start_number is not None:
            result['StartNumber'] = self.start_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('StartNumber') is not None:
            self.start_number = m.get('StartNumber')
        return self


class CreateMediaConvertTaskRequestTargets(TeaModel):
    def __init__(
        self,
        audio: TargetAudio = None,
        container: str = None,
        image: TargetImage = None,
        segment: CreateMediaConvertTaskRequestTargetsSegment = None,
        speed: float = None,
        strip_metadata: bool = None,
        subtitle: TargetSubtitle = None,
        uri: str = None,
        video: TargetVideo = None,
    ):
        self.audio = audio
        self.container = container
        self.image = image
        self.segment = segment
        self.speed = speed
        self.strip_metadata = strip_metadata
        self.subtitle = subtitle
        self.uri = uri
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.image:
            self.image.validate()
        if self.segment:
            self.segment.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.container is not None:
            result['Container'] = self.container
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.segment is not None:
            result['Segment'] = self.segment.to_map()
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.strip_metadata is not None:
            result['StripMetadata'] = self.strip_metadata
        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()
        if self.uri is not None:
            result['URI'] = self.uri
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = TargetAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('Container') is not None:
            self.container = m.get('Container')
        if m.get('Image') is not None:
            temp_model = TargetImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('Segment') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsSegment()
            self.segment = temp_model.from_map(m['Segment'])
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StripMetadata') is not None:
            self.strip_metadata = m.get('StripMetadata')
        if m.get('Subtitle') is not None:
            temp_model = TargetSubtitle()
            self.subtitle = temp_model.from_map(m['Subtitle'])
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Video') is not None:
            temp_model = TargetVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class CreateMediaConvertTaskRequest(TeaModel):
    def __init__(
        self,
        alignment_index: int = None,
        credential_config: CredentialConfig = None,
        notification: Notification = None,
        project_name: str = None,
        sources: List[CreateMediaConvertTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        targets: List[CreateMediaConvertTaskRequestTargets] = None,
        user_data: str = None,
    ):
        self.alignment_index = alignment_index
        self.credential_config = credential_config
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.sources = sources
        self.tags = tags
        # This parameter is required.
        self.targets = targets
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment_index is not None:
            result['AlignmentIndex'] = self.alignment_index
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlignmentIndex') is not None:
            self.alignment_index = m.get('AlignmentIndex')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateMediaConvertTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = CreateMediaConvertTaskRequestTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateMediaConvertTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        alignment_index: int = None,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        targets_shrink: str = None,
        user_data: str = None,
    ):
        self.alignment_index = alignment_index
        self.credential_config_shrink = credential_config_shrink
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.targets_shrink = targets_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment_index is not None:
            result['AlignmentIndex'] = self.alignment_index
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlignmentIndex') is not None:
            self.alignment_index = m.get('AlignmentIndex')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateMediaConvertTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateMediaConvertTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMediaConvertTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMediaConvertTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        end_page: int = None,
        first_page: bool = None,
        fit_to_height: bool = None,
        fit_to_width: bool = None,
        hold_line_feed: bool = None,
        image_dpi: int = None,
        long_picture: bool = None,
        long_text: bool = None,
        max_sheet_column: int = None,
        max_sheet_row: int = None,
        notification: Notification = None,
        pages: str = None,
        paper_horizontal: bool = None,
        paper_size: str = None,
        password: str = None,
        project_name: str = None,
        quality: int = None,
        scale_percentage: int = None,
        sheet_count: int = None,
        sheet_index: int = None,
        show_comments: bool = None,
        source_type: str = None,
        source_uri: str = None,
        start_page: int = None,
        tags: Dict[str, Any] = None,
        target_type: str = None,
        target_uri: str = None,
        target_uriprefix: str = None,
        trim_policy: TrimPolicy = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.end_page = end_page
        self.first_page = first_page
        self.fit_to_height = fit_to_height
        self.fit_to_width = fit_to_width
        self.hold_line_feed = hold_line_feed
        self.image_dpi = image_dpi
        self.long_picture = long_picture
        self.long_text = long_text
        self.max_sheet_column = max_sheet_column
        self.max_sheet_row = max_sheet_row
        self.notification = notification
        self.pages = pages
        self.paper_horizontal = paper_horizontal
        self.paper_size = paper_size
        self.password = password
        # This parameter is required.
        self.project_name = project_name
        self.quality = quality
        self.scale_percentage = scale_percentage
        self.sheet_count = sheet_count
        self.sheet_index = sheet_index
        self.show_comments = show_comments
        self.source_type = source_type
        # This parameter is required.
        self.source_uri = source_uri
        self.start_page = start_page
        self.tags = tags
        # This parameter is required.
        self.target_type = target_type
        self.target_uri = target_uri
        self.target_uriprefix = target_uriprefix
        self.trim_policy = trim_policy
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.trim_policy:
            self.trim_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed
        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi
        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture
        if self.long_text is not None:
            result['LongText'] = self.long_text
        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix
        if self.trim_policy is not None:
            result['TrimPolicy'] = self.trim_policy.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')
        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')
        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')
        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')
        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')
        if m.get('TrimPolicy') is not None:
            temp_model = TrimPolicy()
            self.trim_policy = temp_model.from_map(m['TrimPolicy'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        end_page: int = None,
        first_page: bool = None,
        fit_to_height: bool = None,
        fit_to_width: bool = None,
        hold_line_feed: bool = None,
        image_dpi: int = None,
        long_picture: bool = None,
        long_text: bool = None,
        max_sheet_column: int = None,
        max_sheet_row: int = None,
        notification_shrink: str = None,
        pages: str = None,
        paper_horizontal: bool = None,
        paper_size: str = None,
        password: str = None,
        project_name: str = None,
        quality: int = None,
        scale_percentage: int = None,
        sheet_count: int = None,
        sheet_index: int = None,
        show_comments: bool = None,
        source_type: str = None,
        source_uri: str = None,
        start_page: int = None,
        tags_shrink: str = None,
        target_type: str = None,
        target_uri: str = None,
        target_uriprefix: str = None,
        trim_policy_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.end_page = end_page
        self.first_page = first_page
        self.fit_to_height = fit_to_height
        self.fit_to_width = fit_to_width
        self.hold_line_feed = hold_line_feed
        self.image_dpi = image_dpi
        self.long_picture = long_picture
        self.long_text = long_text
        self.max_sheet_column = max_sheet_column
        self.max_sheet_row = max_sheet_row
        self.notification_shrink = notification_shrink
        self.pages = pages
        self.paper_horizontal = paper_horizontal
        self.paper_size = paper_size
        self.password = password
        # This parameter is required.
        self.project_name = project_name
        self.quality = quality
        self.scale_percentage = scale_percentage
        self.sheet_count = sheet_count
        self.sheet_index = sheet_index
        self.show_comments = show_comments
        self.source_type = source_type
        # This parameter is required.
        self.source_uri = source_uri
        self.start_page = start_page
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.target_type = target_type
        self.target_uri = target_uri
        self.target_uriprefix = target_uriprefix
        self.trim_policy_shrink = trim_policy_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed
        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi
        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture
        if self.long_text is not None:
            result['LongText'] = self.long_text
        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix
        if self.trim_policy_shrink is not None:
            result['TrimPolicy'] = self.trim_policy_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')
        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')
        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')
        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')
        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')
        if m.get('TrimPolicy') is not None:
            self.trim_policy_shrink = m.get('TrimPolicy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        service_role: str = None,
        tag: List[CreateProjectRequestTag] = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.description = description
        self.project_max_dataset_count = project_max_dataset_count
        # This parameter is required.
        self.project_name = project_name
        self.service_role = service_role
        self.tag = tag
        self.template_id = template_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateProjectRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        service_role: str = None,
        tag_shrink: str = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.description = description
        self.project_max_dataset_count = project_max_dataset_count
        # This parameter is required.
        self.project_name = project_name
        self.service_role = service_role
        self.tag_shrink = tag_shrink
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: Project = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimilarImageClusteringTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notification: Notification = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateSimilarImageClusteringTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateSimilarImageClusteringTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateSimilarImageClusteringTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSimilarImageClusteringTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSimilarImageClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoryRequest(TeaModel):
    def __init__(
        self,
        address: AddressForStory = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        max_file_count: int = None,
        min_file_count: int = None,
        notification: Notification = None,
        notify_topic_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.address = address
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_file_count = max_file_count
        self.min_file_count = min_file_count
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification
        self.notify_topic_name = notify_topic_name
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name
        self.story_end_time = story_end_time
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.address:
            self.address.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count
        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = AddressForStory()
            self.address = temp_model.from_map(m['Address'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')
        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateStoryShrinkRequest(TeaModel):
    def __init__(
        self,
        address_shrink: str = None,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        max_file_count: int = None,
        min_file_count: int = None,
        notification_shrink: str = None,
        notify_topic_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.address_shrink = address_shrink
        self.custom_id = custom_id
        self.custom_labels_shrink = custom_labels_shrink
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_file_count = max_file_count
        self.min_file_count = min_file_count
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink
        self.notify_topic_name = notify_topic_name
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name
        self.story_end_time = story_end_time
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count
        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')
        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateStoryResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequestActions(TeaModel):
    def __init__(
        self,
        fast_fail_policy: FastFailPolicy = None,
        name: str = None,
        parameters: List[str] = None,
    ):
        self.fast_fail_policy = fast_fail_policy
        # This parameter is required.
        self.name = name
        self.parameters = parameters

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m['FastFailPolicy'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class CreateTriggerRequestNotification(TeaModel):
    def __init__(
        self,
        mns: MNS = None,
    ):
        self.mns = mns

    def validate(self):
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(
        self,
        actions: List[CreateTriggerRequestActions] = None,
        input: Input = None,
        notification: CreateTriggerRequestNotification = None,
        project_name: str = None,
        service_role: str = None,
        tags: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.actions = actions
        # This parameter is required.
        self.input = input
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.service_role = service_role
        self.tags = tags

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = CreateTriggerRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Notification') is not None:
            temp_model = CreateTriggerRequestNotification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateTriggerShrinkRequest(TeaModel):
    def __init__(
        self,
        actions_shrink: str = None,
        input_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        service_role: str = None,
        tags_shrink: str = None,
    ):
        # This parameter is required.
        self.actions_shrink = actions_shrink
        # This parameter is required.
        self.input_shrink = input_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.service_role = service_role
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoLabelClassificationTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        notification: Notification = None,
        project_name: str = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoLabelClassificationTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoLabelClassificationTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoLabelClassificationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVideoLabelClassificationTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVideoLabelClassificationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoModerationTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        interval: int = None,
        max_frames: int = None,
        notification: Notification = None,
        project_name: str = None,
        scenes: List[str] = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.interval = interval
        self.max_frames = max_frames
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.scenes = scenes
        # This parameter is required.
        self.source_uri = source_uri
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes is not None:
            result['Scenes'] = self.scenes
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoModerationTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        interval: int = None,
        max_frames: int = None,
        notification_shrink: str = None,
        project_name: str = None,
        scenes_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.interval = interval
        self.max_frames = max_frames
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.scenes_shrink = scenes_shrink
        # This parameter is required.
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoModerationTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoModerationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVideoModerationTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVideoModerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBatchRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteBindingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteDatasetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLocationDateClusterRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteLocationDateClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLocationDateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLocationDateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLocationDateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStoryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteStoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTriggerRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachOSSBucketRequest(TeaModel):
    def __init__(
        self,
        ossbucket: str = None,
    ):
        # This parameter is required.
        self.ossbucket = ossbucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        return self


class DetachOSSBucketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachOSSBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachOSSBucketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachOSSBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageBodiesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        sensitivity: float = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        self.sensitivity = sensitivity
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageBodiesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        sensitivity: float = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        self.sensitivity = sensitivity
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageBodiesResponseBody(TeaModel):
    def __init__(
        self,
        bodies: List[Body] = None,
        request_id: str = None,
    ):
        self.bodies = bodies
        self.request_id = request_id

    def validate(self):
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bodies = []
        if m.get('Bodies') is not None:
            for k in m.get('Bodies'):
                temp_model = Body()
                self.bodies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageBodiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageBodiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageBodiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCarsRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCarsShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCarsResponseBody(TeaModel):
    def __init__(
        self,
        cars: List[Car] = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.cars = cars
        self.request_id = request_id

    def validate(self):
        if self.cars:
            for k in self.cars:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cars'] = []
        if self.cars is not None:
            for k in self.cars:
                result['Cars'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cars = []
        if m.get('Cars') is not None:
            for k in m.get('Cars'):
                temp_model = Car()
                self.cars.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCarsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageCarsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageCarsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCodesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCodesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCodesResponseBody(TeaModel):
    def __init__(
        self,
        codes: List[Codes] = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.codes = codes
        self.request_id = request_id

    def validate(self):
        if self.codes:
            for k in self.codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Codes'] = []
        if self.codes is not None:
            for k in self.codes:
                result['Codes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.codes = []
        if m.get('Codes') is not None:
            for k in m.get('Codes'):
                temp_model = Codes()
                self.codes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageCodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCroppingRequest(TeaModel):
    def __init__(
        self,
        aspect_ratios: str = None,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.aspect_ratios = aspect_ratios
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCroppingShrinkRequest(TeaModel):
    def __init__(
        self,
        aspect_ratios: str = None,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.aspect_ratios = aspect_ratios
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCroppingResponseBody(TeaModel):
    def __init__(
        self,
        croppings: List[CroppingSuggestion] = None,
        request_id: str = None,
    ):
        self.croppings = croppings
        self.request_id = request_id

    def validate(self):
        if self.croppings:
            for k in self.croppings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Croppings'] = []
        if self.croppings is not None:
            for k in self.croppings:
                result['Croppings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.croppings = []
        if m.get('Croppings') is not None:
            for k in m.get('Croppings'):
                temp_model = CroppingSuggestion()
                self.croppings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCroppingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageCroppingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageCroppingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageFacesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageFacesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageFacesResponseBody(TeaModel):
    def __init__(
        self,
        faces: List[Figure] = None,
        request_id: str = None,
    ):
        self.faces = faces
        self.request_id = request_id

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = Figure()
                self.faces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageFacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageLabelsRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
        threshold: float = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.threshold = threshold

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectImageLabelsShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
        threshold: float = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectImageLabelsResponseBody(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
        request_id: str = None,
    ):
        self.labels = labels
        self.request_id = request_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageLabelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageScoreRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageScoreShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageScoreResponseBodyImageScore(TeaModel):
    def __init__(
        self,
        overall_quality_score: float = None,
    ):
        self.overall_quality_score = overall_quality_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class DetectImageScoreResponseBody(TeaModel):
    def __init__(
        self,
        image_score: DetectImageScoreResponseBodyImageScore = None,
        request_id: str = None,
    ):
        self.image_score = image_score
        self.request_id = request_id

    def validate(self):
        if self.image_score:
            self.image_score.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            temp_model = DetectImageScoreResponseBodyImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageScoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageTextsRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageTextsShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageTextsResponseBody(TeaModel):
    def __init__(
        self,
        ocrcontents: List[OCRContents] = None,
        ocrtexts: str = None,
        request_id: str = None,
    ):
        self.ocrcontents = ocrcontents
        self.ocrtexts = ocrtexts
        self.request_id = request_id

    def validate(self):
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.ocrtexts is not None:
            result['OCRTexts'] = self.ocrtexts
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('OCRTexts') is not None:
            self.ocrtexts = m.get('OCRTexts')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageTextsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageTextsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectImageTextsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectMediaMetaRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectMediaMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectMediaMetaResponseBody(TeaModel):
    def __init__(
        self,
        addresses: List[Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        audio_streams: List[AudioStream] = None,
        bitrate: int = None,
        composer: str = None,
        duration: float = None,
        format_long_name: str = None,
        format_name: str = None,
        language: str = None,
        lat_long: str = None,
        performer: str = None,
        produce_time: str = None,
        program_count: int = None,
        request_id: str = None,
        size: int = None,
        start_time: float = None,
        stream_count: int = None,
        subtitles: List[SubtitleStream] = None,
        title: str = None,
        video_height: int = None,
        video_streams: List[VideoStream] = None,
        video_width: int = None,
    ):
        self.addresses = addresses
        self.album = album
        self.album_artist = album_artist
        self.artist = artist
        self.audio_streams = audio_streams
        self.bitrate = bitrate
        self.composer = composer
        self.duration = duration
        self.format_long_name = format_long_name
        self.format_name = format_name
        self.language = language
        self.lat_long = lat_long
        self.performer = performer
        self.produce_time = produce_time
        self.program_count = program_count
        self.request_id = request_id
        self.size = size
        self.start_time = start_time
        self.stream_count = stream_count
        self.subtitles = subtitles
        self.title = title
        self.video_height = video_height
        self.video_streams = video_streams
        self.video_width = video_width

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.language is not None:
            result['Language'] = self.language
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.program_count is not None:
            result['ProgramCount'] = self.program_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class DetectMediaMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectMediaMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectMediaMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectTextAnomalyRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DetectTextAnomalyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        suggestion: str = None,
    ):
        self.request_id = request_id
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DetectTextAnomalyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectTextAnomalyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectTextAnomalyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncodeBlindWatermarkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        image_quality: int = None,
        project_name: str = None,
        source_uri: str = None,
        strength_level: str = None,
        target_uri: str = None,
    ):
        self.content = content
        self.image_quality = image_quality
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.source_uri = source_uri
        self.strength_level = strength_level
        # This parameter is required.
        self.target_uri = target_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.strength_level is not None:
            result['StrengthLevel'] = self.strength_level
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StrengthLevel') is not None:
            self.strength_level = m.get('StrengthLevel')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        return self


class EncodeBlindWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncodeBlindWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EncodeBlindWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EncodeBlindWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractDocumentTextRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_type: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        self.source_type = source_type
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class ExtractDocumentTextShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_type: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        self.source_type = source_type
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class ExtractDocumentTextResponseBody(TeaModel):
    def __init__(
        self,
        document_text: str = None,
        request_id: str = None,
    ):
        self.document_text = document_text
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_text is not None:
            result['DocumentText'] = self.document_text
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentText') is not None:
            self.document_text = m.get('DocumentText')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractDocumentTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExtractDocumentTextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExtractDocumentTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FuzzyQueryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query: str = None,
        sort: str = None,
        with_fields: List[str] = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.query = query
        self.sort = sort
        self.with_fields = with_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class FuzzyQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query: str = None,
        sort: str = None,
        with_fields_shrink: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.query = query
        self.sort = sort
        self.with_fields_shrink = with_fields_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class FuzzyQueryResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        next_token: str = None,
        request_id: str = None,
        total_hits: int = None,
    ):
        self.files = files
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id
        self.total_hits = total_hits

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_hits is not None:
            result['TotalHits'] = self.total_hits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalHits') is not None:
            self.total_hits = m.get('TotalHits')
        return self


class FuzzyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FuzzyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FuzzyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVideoPlaylistRequestSourceSubtitles(TeaModel):
    def __init__(
        self,
        language: str = None,
        uri: str = None,
    ):
        self.language = language
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistRequestTargets(TeaModel):
    def __init__(
        self,
        audio: TargetAudio = None,
        duration: float = None,
        initial_segments: List[float] = None,
        initial_transcode: float = None,
        subtitle: TargetSubtitle = None,
        tags: Dict[str, str] = None,
        transcode_ahead: int = None,
        uri: str = None,
        video: TargetVideo = None,
    ):
        self.audio = audio
        self.duration = duration
        self.initial_segments = initial_segments
        self.initial_transcode = initial_transcode
        self.subtitle = subtitle
        self.tags = tags
        self.transcode_ahead = transcode_ahead
        self.uri = uri
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.initial_segments is not None:
            result['InitialSegments'] = self.initial_segments
        if self.initial_transcode is not None:
            result['InitialTranscode'] = self.initial_transcode
        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.transcode_ahead is not None:
            result['TranscodeAhead'] = self.transcode_ahead
        if self.uri is not None:
            result['URI'] = self.uri
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = TargetAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InitialSegments') is not None:
            self.initial_segments = m.get('InitialSegments')
        if m.get('InitialTranscode') is not None:
            self.initial_transcode = m.get('InitialTranscode')
        if m.get('Subtitle') is not None:
            temp_model = TargetSubtitle()
            self.subtitle = temp_model.from_map(m['Subtitle'])
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TranscodeAhead') is not None:
            self.transcode_ahead = m.get('TranscodeAhead')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Video') is not None:
            temp_model = TargetVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class GenerateVideoPlaylistRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        master_uri: str = None,
        notification: Notification = None,
        overwrite_policy: str = None,
        project_name: str = None,
        source_duration: float = None,
        source_start_time: float = None,
        source_subtitles: List[GenerateVideoPlaylistRequestSourceSubtitles] = None,
        source_uri: str = None,
        tags: Dict[str, str] = None,
        targets: List[GenerateVideoPlaylistRequestTargets] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.master_uri = master_uri
        self.notification = notification
        self.overwrite_policy = overwrite_policy
        # This parameter is required.
        self.project_name = project_name
        self.source_duration = source_duration
        self.source_start_time = source_start_time
        self.source_subtitles = source_subtitles
        # This parameter is required.
        self.source_uri = source_uri
        self.tags = tags
        # This parameter is required.
        self.targets = targets
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.source_subtitles:
            for k in self.source_subtitles:
                if k:
                    k.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.overwrite_policy is not None:
            result['OverwritePolicy'] = self.overwrite_policy
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_duration is not None:
            result['SourceDuration'] = self.source_duration
        if self.source_start_time is not None:
            result['SourceStartTime'] = self.source_start_time
        result['SourceSubtitles'] = []
        if self.source_subtitles is not None:
            for k in self.source_subtitles:
                result['SourceSubtitles'].append(k.to_map() if k else None)
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('OverwritePolicy') is not None:
            self.overwrite_policy = m.get('OverwritePolicy')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceDuration') is not None:
            self.source_duration = m.get('SourceDuration')
        if m.get('SourceStartTime') is not None:
            self.source_start_time = m.get('SourceStartTime')
        self.source_subtitles = []
        if m.get('SourceSubtitles') is not None:
            for k in m.get('SourceSubtitles'):
                temp_model = GenerateVideoPlaylistRequestSourceSubtitles()
                self.source_subtitles.append(temp_model.from_map(k))
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = GenerateVideoPlaylistRequestTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GenerateVideoPlaylistShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        master_uri: str = None,
        notification_shrink: str = None,
        overwrite_policy: str = None,
        project_name: str = None,
        source_duration: float = None,
        source_start_time: float = None,
        source_subtitles_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        targets_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.master_uri = master_uri
        self.notification_shrink = notification_shrink
        self.overwrite_policy = overwrite_policy
        # This parameter is required.
        self.project_name = project_name
        self.source_duration = source_duration
        self.source_start_time = source_start_time
        self.source_subtitles_shrink = source_subtitles_shrink
        # This parameter is required.
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.targets_shrink = targets_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.overwrite_policy is not None:
            result['OverwritePolicy'] = self.overwrite_policy
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_duration is not None:
            result['SourceDuration'] = self.source_duration
        if self.source_start_time is not None:
            result['SourceStartTime'] = self.source_start_time
        if self.source_subtitles_shrink is not None:
            result['SourceSubtitles'] = self.source_subtitles_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('OverwritePolicy') is not None:
            self.overwrite_policy = m.get('OverwritePolicy')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceDuration') is not None:
            self.source_duration = m.get('SourceDuration')
        if m.get('SourceStartTime') is not None:
            self.source_start_time = m.get('SourceStartTime')
        if m.get('SourceSubtitles') is not None:
            self.source_subtitles_shrink = m.get('SourceSubtitles')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GenerateVideoPlaylistResponseBodyAudioPlaylist(TeaModel):
    def __init__(
        self,
        channels: int = None,
        token: str = None,
        uri: str = None,
    ):
        self.channels = channels
        # 转码生成的Token。用于LiveTranscoding访问的参数。
        self.token = token
        # 输出m3u8的OSS地址。地址规则为 Target.URI + ".m3u8“， 其中Target.URI为输入参数中视频转码输出地址前缀。
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistResponseBodySubtitlePlaylist(TeaModel):
    def __init__(
        self,
        index: int = None,
        language: str = None,
        token: str = None,
        uri: str = None,
    ):
        # 字幕流编号，从0开始。
        self.index = index
        # 视频源中字幕流的语言。
        self.language = language
        # 转码生成的Token。用于LiveTranscoding访问的参数。
        self.token = token
        # 输出m3u8的OSS地址。地址规则为 Target.URI + “_” + Index + ".m3u8“， 其中Target.URI为输入参数中视频转码输出地址前缀。
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistResponseBodyVideoPlaylist(TeaModel):
    def __init__(
        self,
        frame_rate: str = None,
        resolution: str = None,
        token: str = None,
        uri: str = None,
    ):
        self.frame_rate = frame_rate
        self.resolution = resolution
        # 转码生成的Token。用于LiveTranscoding访问的参数。
        self.token = token
        # 输出m3u8的OSS地址。地址规则为 Target.URI + ".m3u8“， 其中Target.URI为输入参数中视频转码输出地址前缀。
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistResponseBody(TeaModel):
    def __init__(
        self,
        audio_playlist: List[GenerateVideoPlaylistResponseBodyAudioPlaylist] = None,
        duration: float = None,
        master_uri: str = None,
        request_id: str = None,
        subtitle_playlist: List[GenerateVideoPlaylistResponseBodySubtitlePlaylist] = None,
        token: str = None,
        video_playlist: List[GenerateVideoPlaylistResponseBodyVideoPlaylist] = None,
    ):
        # 转码文件列表。
        self.audio_playlist = audio_playlist
        self.duration = duration
        self.master_uri = master_uri
        self.request_id = request_id
        # 转码文件列表。
        self.subtitle_playlist = subtitle_playlist
        self.token = token
        # 转码文件列表。
        self.video_playlist = video_playlist

    def validate(self):
        if self.audio_playlist:
            for k in self.audio_playlist:
                if k:
                    k.validate()
        if self.subtitle_playlist:
            for k in self.subtitle_playlist:
                if k:
                    k.validate()
        if self.video_playlist:
            for k in self.video_playlist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioPlaylist'] = []
        if self.audio_playlist is not None:
            for k in self.audio_playlist:
                result['AudioPlaylist'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubtitlePlaylist'] = []
        if self.subtitle_playlist is not None:
            for k in self.subtitle_playlist:
                result['SubtitlePlaylist'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token
        result['VideoPlaylist'] = []
        if self.video_playlist is not None:
            for k in self.video_playlist:
                result['VideoPlaylist'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_playlist = []
        if m.get('AudioPlaylist') is not None:
            for k in m.get('AudioPlaylist'):
                temp_model = GenerateVideoPlaylistResponseBodyAudioPlaylist()
                self.audio_playlist.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subtitle_playlist = []
        if m.get('SubtitlePlaylist') is not None:
            for k in m.get('SubtitlePlaylist'):
                temp_model = GenerateVideoPlaylistResponseBodySubtitlePlaylist()
                self.subtitle_playlist.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            self.token = m.get('Token')
        self.video_playlist = []
        if m.get('VideoPlaylist') is not None:
            for k in m.get('VideoPlaylist'):
                temp_model = GenerateVideoPlaylistResponseBodyVideoPlaylist()
                self.video_playlist.append(temp_model.from_map(k))
        return self


class GenerateVideoPlaylistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateVideoPlaylistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateVideoPlaylistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateWebofficeTokenRequest(TeaModel):
    def __init__(
        self,
        cache_preview: bool = None,
        credential_config: CredentialConfig = None,
        external_uploaded: bool = None,
        filename: str = None,
        hidecmb: bool = None,
        notification: Notification = None,
        notify_topic_name: str = None,
        password: str = None,
        permission: WebofficePermission = None,
        preview_pages: int = None,
        project_name: str = None,
        referer: str = None,
        source_uri: str = None,
        user: WebofficeUser = None,
        user_data: str = None,
        watermark: WebofficeWatermark = None,
    ):
        self.cache_preview = cache_preview
        self.credential_config = credential_config
        self.external_uploaded = external_uploaded
        self.filename = filename
        self.hidecmb = hidecmb
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification
        self.notify_topic_name = notify_topic_name
        self.password = password
        self.permission = permission
        self.preview_pages = preview_pages
        # This parameter is required.
        self.project_name = project_name
        self.referer = referer
        # This parameter is required.
        self.source_uri = source_uri
        self.user = user
        self.user_data = user_data
        self.watermark = watermark

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.permission:
            self.permission.validate()
        if self.user:
            self.user.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.password is not None:
            result['Password'] = self.password
        if self.permission is not None:
            result['Permission'] = self.permission.to_map()
        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Permission') is not None:
            temp_model = WebofficePermission()
            self.permission = temp_model.from_map(m['Permission'])
        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('User') is not None:
            temp_model = WebofficeUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Watermark') is not None:
            temp_model = WebofficeWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class GenerateWebofficeTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        cache_preview: bool = None,
        credential_config_shrink: str = None,
        external_uploaded: bool = None,
        filename: str = None,
        hidecmb: bool = None,
        notification_shrink: str = None,
        notify_topic_name: str = None,
        password: str = None,
        permission_shrink: str = None,
        preview_pages: int = None,
        project_name: str = None,
        referer: str = None,
        source_uri: str = None,
        user_shrink: str = None,
        user_data: str = None,
        watermark_shrink: str = None,
    ):
        self.cache_preview = cache_preview
        self.credential_config_shrink = credential_config_shrink
        self.external_uploaded = external_uploaded
        self.filename = filename
        self.hidecmb = hidecmb
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink
        self.notify_topic_name = notify_topic_name
        self.password = password
        self.permission_shrink = permission_shrink
        self.preview_pages = preview_pages
        # This parameter is required.
        self.project_name = project_name
        self.referer = referer
        # This parameter is required.
        self.source_uri = source_uri
        self.user_shrink = user_shrink
        self.user_data = user_data
        self.watermark_shrink = watermark_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.password is not None:
            result['Password'] = self.password
        if self.permission_shrink is not None:
            result['Permission'] = self.permission_shrink
        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.watermark_shrink is not None:
            result['Watermark'] = self.watermark_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Permission') is not None:
            self.permission_shrink = m.get('Permission')
        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Watermark') is not None:
            self.watermark_shrink = m.get('Watermark')
        return self


class GenerateWebofficeTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
        request_id: str = None,
        weboffice_url: str = None,
    ):
        self.access_token = access_token
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token
        self.refresh_token_expired_time = refresh_token_expired_time
        self.request_id = request_id
        self.weboffice_url = weboffice_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.weboffice_url is not None:
            result['WebofficeURL'] = self.weboffice_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebofficeURL') is not None:
            self.weboffice_url = m.get('WebofficeURL')
        return self


class GenerateWebofficeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateWebofficeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetBatchResponseBody(TeaModel):
    def __init__(
        self,
        batch: DataIngestion = None,
        request_id: str = None,
    ):
        self.batch = batch
        self.request_id = request_id

    def validate(self):
        if self.batch:
            self.batch.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch is not None:
            result['Batch'] = self.batch.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Batch') is not None:
            temp_model = DataIngestion()
            self.batch = temp_model.from_map(m['Batch'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetBindingResponseBody(TeaModel):
    def __init__(
        self,
        binding: Binding = None,
        request_id: str = None,
    ):
        self.binding = binding
        self.request_id = request_id

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = Binding()
            self.binding = temp_model.from_map(m['Binding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDRMLicenseRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        protection_system: str = None,
    ):
        self.key_id = key_id
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.protection_system = protection_system

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.protection_system is not None:
            result['ProtectionSystem'] = self.protection_system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProtectionSystem') is not None:
            self.protection_system = m.get('ProtectionSystem')
        return self


class GetDRMLicenseResponseBody(TeaModel):
    def __init__(
        self,
        device_info: str = None,
        license: str = None,
        request_id: str = None,
        states: int = None,
    ):
        self.device_info = device_info
        self.license = license
        self.request_id = request_id
        self.states = states

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        if self.license is not None:
            result['License'] = self.license
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.states is not None:
            result['States'] = self.states
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('States') is not None:
            self.states = m.get('States')
        return self


class GetDRMLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDRMLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDRMLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        with_statistics: bool = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset: Dataset = None,
        request_id: str = None,
    ):
        self.dataset = dataset
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDecodeBlindWatermarkResultRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetDecodeBlindWatermarkResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.content = content
        self.end_time = end_time
        self.event_id = event_id
        self.message = message
        self.project_name = project_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetDecodeBlindWatermarkResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDecodeBlindWatermarkResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDecodeBlindWatermarkResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFigureClusterRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetFigureClusterResponseBody(TeaModel):
    def __init__(
        self,
        figure_cluster: FigureCluster = None,
        request_id: str = None,
    ):
        self.figure_cluster = figure_cluster
        self.request_id = request_id

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureCluster') is not None:
            temp_model = FigureCluster()
            self.figure_cluster = temp_model.from_map(m['FigureCluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFigureClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFigureClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
        with_fields: List[str] = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uri = uri
        self.with_fields = with_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class GetFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
        with_fields_shrink: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.uri = uri
        self.with_fields_shrink = with_fields_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class GetFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        request_id: str = None,
    ):
        self.files = files
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageModerationResultRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetImageModerationResultResponseBodyModerationResultFramesBlockFrames(TeaModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        rate: float = None,
    ):
        self.label = label
        self.offset = offset
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class GetImageModerationResultResponseBodyModerationResultFrames(TeaModel):
    def __init__(
        self,
        block_frames: List[GetImageModerationResultResponseBodyModerationResultFramesBlockFrames] = None,
        total_count: int = None,
    ):
        self.block_frames = block_frames
        self.total_count = total_count

    def validate(self):
        if self.block_frames:
            for k in self.block_frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockFrames'] = []
        if self.block_frames is not None:
            for k in self.block_frames:
                result['BlockFrames'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_frames = []
        if m.get('BlockFrames') is not None:
            for k in m.get('BlockFrames'):
                temp_model = GetImageModerationResultResponseBodyModerationResultFramesBlockFrames()
                self.block_frames.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetImageModerationResultResponseBodyModerationResult(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        frames: GetImageModerationResultResponseBodyModerationResultFrames = None,
        suggestion: str = None,
        uri: str = None,
    ):
        self.categories = categories
        self.frames = frames
        self.suggestion = suggestion
        self.uri = uri

    def validate(self):
        if self.frames:
            self.frames.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.frames is not None:
            result['Frames'] = self.frames.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Frames') is not None:
            temp_model = GetImageModerationResultResponseBodyModerationResultFrames()
            self.frames = temp_model.from_map(m['Frames'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetImageModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        moderation_result: GetImageModerationResultResponseBodyModerationResult = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.end_time = end_time
        self.event_id = event_id
        self.message = message
        self.moderation_result = moderation_result
        self.project_name = project_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.user_data = user_data

    def validate(self):
        if self.moderation_result:
            self.moderation_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.moderation_result is not None:
            result['ModerationResult'] = self.moderation_result.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModerationResult') is not None:
            temp_model = GetImageModerationResultResponseBodyModerationResult()
            self.moderation_result = temp_model.from_map(m['ModerationResult'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetImageModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetImageModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSBucketAttachmentRequest(TeaModel):
    def __init__(
        self,
        ossbucket: str = None,
    ):
        # This parameter is required.
        self.ossbucket = ossbucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        return self


class GetOSSBucketAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        project_name: str = None,
        request_id: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.project_name = project_name
        self.request_id = request_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetOSSBucketAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOSSBucketAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOSSBucketAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        with_statistics: bool = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: Project = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetStoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        story: Story = None,
    ):
        self.request_id = request_id
        self.story = story

    def validate(self):
        if self.story:
            self.story.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.story is not None:
            result['Story'] = self.story.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Story') is not None:
            temp_model = Story()
            self.story = temp_model.from_map(m['Story'])
        return self


class GetStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        request_definition: bool = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        self.request_definition = request_definition
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        progress: int = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        task_id: str = None,
        task_request_definition: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.end_time = end_time
        self.event_id = event_id
        self.message = message
        self.progress = progress
        self.project_name = project_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.tags = tags
        self.task_id = task_id
        self.task_request_definition = task_request_definition
        self.task_type = task_type
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_request_definition is not None:
            result['TaskRequestDefinition'] = self.task_request_definition
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskRequestDefinition') is not None:
            self.task_request_definition = m.get('TaskRequestDefinition')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTriggerRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trigger: DataIngestion = None,
    ):
        self.request_id = request_id
        self.trigger = trigger

    def validate(self):
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Trigger') is not None:
            temp_model = DataIngestion()
            self.trigger = temp_model.from_map(m['Trigger'])
        return self


class GetTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoLabelClassificationResultRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetVideoLabelClassificationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        labels: List[Label] = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.end_time = end_time
        self.event_id = event_id
        self.labels = labels
        self.message = message
        self.project_name = project_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.user_data = user_data

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetVideoLabelClassificationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoLabelClassificationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVideoLabelClassificationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoModerationResultRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames(TeaModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        rate: float = None,
    ):
        self.label = label
        self.offset = offset
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class GetVideoModerationResultResponseBodyModerationResultFrames(TeaModel):
    def __init__(
        self,
        block_frames: List[GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames] = None,
        total_count: int = None,
    ):
        self.block_frames = block_frames
        self.total_count = total_count

    def validate(self):
        if self.block_frames:
            for k in self.block_frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockFrames'] = []
        if self.block_frames is not None:
            for k in self.block_frames:
                result['BlockFrames'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_frames = []
        if m.get('BlockFrames') is not None:
            for k in m.get('BlockFrames'):
                temp_model = GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames()
                self.block_frames.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetVideoModerationResultResponseBodyModerationResult(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        frames: GetVideoModerationResultResponseBodyModerationResultFrames = None,
        suggestion: str = None,
        uri: str = None,
    ):
        self.categories = categories
        self.frames = frames
        self.suggestion = suggestion
        self.uri = uri

    def validate(self):
        if self.frames:
            self.frames.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.frames is not None:
            result['Frames'] = self.frames.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Frames') is not None:
            temp_model = GetVideoModerationResultResponseBodyModerationResultFrames()
            self.frames = temp_model.from_map(m['Frames'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetVideoModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        moderation_result: GetVideoModerationResultResponseBodyModerationResult = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.end_time = end_time
        self.event_id = event_id
        self.message = message
        self.moderation_result = moderation_result
        self.project_name = project_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.user_data = user_data

    def validate(self):
        if self.moderation_result:
            self.moderation_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.moderation_result is not None:
            result['ModerationResult'] = self.moderation_result.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModerationResult') is not None:
            temp_model = GetVideoModerationResultResponseBodyModerationResult()
            self.moderation_result = temp_model.from_map(m['ModerationResult'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetVideoModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVideoModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file: InputFile = None,
        notification: Notification = None,
        project_name: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.file = file
        self.notification = notification
        # This parameter is required.
        self.project_name = project_name
        self.user_data = user_data

    def validate(self):
        if self.file:
            self.file.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file is not None:
            result['File'] = self.file.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            temp_model = InputFile()
            self.file = temp_model.from_map(m['File'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class IndexFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.file_shrink = file_shrink
        self.notification_shrink = notification_shrink
        # This parameter is required.
        self.project_name = project_name
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file_shrink is not None:
            result['File'] = self.file_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            self.file_shrink = m.get('File')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class IndexFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IndexFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IndexFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBatchesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        state: str = None,
        tag_selector: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.state = state
        self.tag_selector = tag_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.state is not None:
            result['State'] = self.state
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        return self


class ListBatchesResponseBody(TeaModel):
    def __init__(
        self,
        batches: List[DataIngestion] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.batches = batches
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.batches:
            for k in self.batches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Batches'] = []
        if self.batches is not None:
            for k in self.batches:
                result['Batches'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batches = []
        if m.get('Batches') is not None:
            for k in m.get('Batches'):
                temp_model = DataIngestion()
                self.batches.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBatchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBatchesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBatchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(
        self,
        bindings: List[Binding] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.bindings = bindings
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = Binding()
                self.bindings.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
        project_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.prefix = prefix
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListDatasetsResponseBody(TeaModel):
    def __init__(
        self,
        datasets: List[Dataset] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.datasets = datasets
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = Dataset()
                self.datasets.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
        tag: List[ListProjectsRequestTag] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.prefix = prefix
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListProjectsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListProjectsShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
        tag_shrink: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.prefix = prefix
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        projects: List[Project] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.projects = projects
        self.request_id = request_id

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # This parameter is required.
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[RegionType] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = RegionType()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        end_time_range: TimeRange = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        request_definition: bool = None,
        sort: str = None,
        start_time_range: TimeRange = None,
        status: str = None,
        tag_selector: str = None,
        task_types: List[str] = None,
    ):
        self.end_time_range = end_time_range
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.request_definition = request_definition
        self.sort = sort
        self.start_time_range = start_time_range
        self.status = status
        self.tag_selector = tag_selector
        self.task_types = task_types

    def validate(self):
        if self.end_time_range:
            self.end_time_range.validate()
        if self.start_time_range:
            self.start_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_range is not None:
            result['EndTimeRange'] = self.end_time_range.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time_range is not None:
            result['StartTimeRange'] = self.start_time_range.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        if self.task_types is not None:
            result['TaskTypes'] = self.task_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            temp_model = TimeRange()
            self.end_time_range = temp_model.from_map(m['EndTimeRange'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTimeRange') is not None:
            temp_model = TimeRange()
            self.start_time_range = temp_model.from_map(m['StartTimeRange'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        end_time_range_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        request_definition: bool = None,
        sort: str = None,
        start_time_range_shrink: str = None,
        status: str = None,
        tag_selector: str = None,
        task_types_shrink: str = None,
    ):
        self.end_time_range_shrink = end_time_range_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.request_definition = request_definition
        self.sort = sort
        self.start_time_range_shrink = start_time_range_shrink
        self.status = status
        self.tag_selector = tag_selector
        self.task_types_shrink = task_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_range_shrink is not None:
            result['EndTimeRange'] = self.end_time_range_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time_range_shrink is not None:
            result['StartTimeRange'] = self.start_time_range_shrink
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        if self.task_types_shrink is not None:
            result['TaskTypes'] = self.task_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            self.end_time_range_shrink = m.get('EndTimeRange')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTimeRange') is not None:
            self.start_time_range_shrink = m.get('StartTimeRange')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        if m.get('TaskTypes') is not None:
            self.task_types_shrink = m.get('TaskTypes')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        project_name: str = None,
        request_id: str = None,
        tasks: List[TaskInfo] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.project_name = project_name
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = TaskInfo()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        state: str = None,
        tag_selector: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.state = state
        self.tag_selector = tag_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.state is not None:
            result['State'] = self.state
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        return self


class ListTriggersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        triggers: List[DataIngestion] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = DataIngestion()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTriggersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFigureClustersRequest(TeaModel):
    def __init__(
        self,
        create_time_range: TimeRange = None,
        custom_labels: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        update_time_range: TimeRange = None,
        with_total_count: bool = None,
    ):
        self.create_time_range = create_time_range
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.update_time_range = update_time_range
        self.with_total_count = with_total_count

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.update_time_range:
            self.update_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.update_time_range is not None:
            result['UpdateTimeRange'] = self.update_time_range.to_map()
        if self.with_total_count is not None:
            result['WithTotalCount'] = self.with_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('UpdateTimeRange') is not None:
            temp_model = TimeRange()
            self.update_time_range = temp_model.from_map(m['UpdateTimeRange'])
        if m.get('WithTotalCount') is not None:
            self.with_total_count = m.get('WithTotalCount')
        return self


class QueryFigureClustersShrinkRequest(TeaModel):
    def __init__(
        self,
        create_time_range_shrink: str = None,
        custom_labels: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        update_time_range_shrink: str = None,
        with_total_count: bool = None,
    ):
        self.create_time_range_shrink = create_time_range_shrink
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.update_time_range_shrink = update_time_range_shrink
        self.with_total_count = with_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.update_time_range_shrink is not None:
            result['UpdateTimeRange'] = self.update_time_range_shrink
        if self.with_total_count is not None:
            result['WithTotalCount'] = self.with_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('UpdateTimeRange') is not None:
            self.update_time_range_shrink = m.get('UpdateTimeRange')
        if m.get('WithTotalCount') is not None:
            self.with_total_count = m.get('WithTotalCount')
        return self


class QueryFigureClustersResponseBody(TeaModel):
    def __init__(
        self,
        figure_clusters: List[FigureCluster] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.figure_clusters = figure_clusters
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.figure_clusters:
            for k in self.figure_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FigureClusters'] = []
        if self.figure_clusters is not None:
            for k in self.figure_clusters:
                result['FigureClusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figure_clusters = []
        if m.get('FigureClusters') is not None:
            for k in m.get('FigureClusters'):
                temp_model = FigureCluster()
                self.figure_clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryFigureClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFigureClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryFigureClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocationDateClustersRequest(TeaModel):
    def __init__(
        self,
        address: Address = None,
        create_time_range: TimeRange = None,
        custom_labels: str = None,
        dataset_name: str = None,
        location_date_cluster_end_time_range: TimeRange = None,
        location_date_cluster_levels: List[str] = None,
        location_date_cluster_start_time_range: TimeRange = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        title: str = None,
        update_time_range: TimeRange = None,
    ):
        self.address = address
        self.create_time_range = create_time_range
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.location_date_cluster_end_time_range = location_date_cluster_end_time_range
        self.location_date_cluster_levels = location_date_cluster_levels
        self.location_date_cluster_start_time_range = location_date_cluster_start_time_range
        self.max_results = max_results
        self.next_token = next_token
        self.object_id = object_id
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.title = title
        self.update_time_range = update_time_range

    def validate(self):
        if self.address:
            self.address.validate()
        if self.create_time_range:
            self.create_time_range.validate()
        if self.location_date_cluster_end_time_range:
            self.location_date_cluster_end_time_range.validate()
        if self.location_date_cluster_start_time_range:
            self.location_date_cluster_start_time_range.validate()
        if self.update_time_range:
            self.update_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.location_date_cluster_end_time_range is not None:
            result['LocationDateClusterEndTimeRange'] = self.location_date_cluster_end_time_range.to_map()
        if self.location_date_cluster_levels is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels
        if self.location_date_cluster_start_time_range is not None:
            result['LocationDateClusterStartTimeRange'] = self.location_date_cluster_start_time_range.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_range is not None:
            result['UpdateTimeRange'] = self.update_time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = Address()
            self.address = temp_model.from_map(m['Address'])
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('LocationDateClusterEndTimeRange') is not None:
            temp_model = TimeRange()
            self.location_date_cluster_end_time_range = temp_model.from_map(m['LocationDateClusterEndTimeRange'])
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels = m.get('LocationDateClusterLevels')
        if m.get('LocationDateClusterStartTimeRange') is not None:
            temp_model = TimeRange()
            self.location_date_cluster_start_time_range = temp_model.from_map(m['LocationDateClusterStartTimeRange'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeRange') is not None:
            temp_model = TimeRange()
            self.update_time_range = temp_model.from_map(m['UpdateTimeRange'])
        return self


class QueryLocationDateClustersShrinkRequest(TeaModel):
    def __init__(
        self,
        address_shrink: str = None,
        create_time_range_shrink: str = None,
        custom_labels: str = None,
        dataset_name: str = None,
        location_date_cluster_end_time_range_shrink: str = None,
        location_date_cluster_levels_shrink: str = None,
        location_date_cluster_start_time_range_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        title: str = None,
        update_time_range_shrink: str = None,
    ):
        self.address_shrink = address_shrink
        self.create_time_range_shrink = create_time_range_shrink
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.location_date_cluster_end_time_range_shrink = location_date_cluster_end_time_range_shrink
        self.location_date_cluster_levels_shrink = location_date_cluster_levels_shrink
        self.location_date_cluster_start_time_range_shrink = location_date_cluster_start_time_range_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.object_id = object_id
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.title = title
        self.update_time_range_shrink = update_time_range_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.location_date_cluster_end_time_range_shrink is not None:
            result['LocationDateClusterEndTimeRange'] = self.location_date_cluster_end_time_range_shrink
        if self.location_date_cluster_levels_shrink is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels_shrink
        if self.location_date_cluster_start_time_range_shrink is not None:
            result['LocationDateClusterStartTimeRange'] = self.location_date_cluster_start_time_range_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_range_shrink is not None:
            result['UpdateTimeRange'] = self.update_time_range_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('LocationDateClusterEndTimeRange') is not None:
            self.location_date_cluster_end_time_range_shrink = m.get('LocationDateClusterEndTimeRange')
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels_shrink = m.get('LocationDateClusterLevels')
        if m.get('LocationDateClusterStartTimeRange') is not None:
            self.location_date_cluster_start_time_range_shrink = m.get('LocationDateClusterStartTimeRange')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeRange') is not None:
            self.update_time_range_shrink = m.get('UpdateTimeRange')
        return self


class QueryLocationDateClustersResponseBody(TeaModel):
    def __init__(
        self,
        location_date_clusters: List[LocationDateCluster] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.location_date_clusters = location_date_clusters
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.location_date_clusters:
            for k in self.location_date_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationDateClusters'] = []
        if self.location_date_clusters is not None:
            for k in self.location_date_clusters:
                result['LocationDateClusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.location_date_clusters = []
        if m.get('LocationDateClusters') is not None:
            for k in m.get('LocationDateClusters'):
                temp_model = LocationDateCluster()
                self.location_date_clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryLocationDateClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLocationDateClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryLocationDateClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySimilarImageClustersRequest(TeaModel):
    def __init__(
        self,
        custom_labels: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
    ):
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class QuerySimilarImageClustersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        similar_image_clusters: List[SimilarImageCluster] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.similar_image_clusters = similar_image_clusters

    def validate(self):
        if self.similar_image_clusters:
            for k in self.similar_image_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimilarImageClusters'] = []
        if self.similar_image_clusters is not None:
            for k in self.similar_image_clusters:
                result['SimilarImageClusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.similar_image_clusters = []
        if m.get('SimilarImageClusters') is not None:
            for k in m.get('SimilarImageClusters'):
                temp_model = SimilarImageCluster()
                self.similar_image_clusters.append(temp_model.from_map(k))
        return self


class QuerySimilarImageClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySimilarImageClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySimilarImageClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStoriesRequest(TeaModel):
    def __init__(
        self,
        create_time_range: TimeRange = None,
        custom_labels: str = None,
        dataset_name: str = None,
        figure_cluster_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        story_end_time_range: TimeRange = None,
        story_name: str = None,
        story_start_time_range: TimeRange = None,
        story_sub_type: str = None,
        story_type: str = None,
        with_empty_stories: bool = None,
    ):
        self.create_time_range = create_time_range
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.figure_cluster_ids = figure_cluster_ids
        self.max_results = max_results
        self.next_token = next_token
        self.object_id = object_id
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.story_end_time_range = story_end_time_range
        self.story_name = story_name
        self.story_start_time_range = story_start_time_range
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.with_empty_stories = with_empty_stories

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.story_end_time_range:
            self.story_end_time_range.validate()
        if self.story_start_time_range:
            self.story_start_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.story_end_time_range is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range.to_map()
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time_range is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range.to_map()
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StoryEndTimeRange') is not None:
            temp_model = TimeRange()
            self.story_end_time_range = temp_model.from_map(m['StoryEndTimeRange'])
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTimeRange') is not None:
            temp_model = TimeRange()
            self.story_start_time_range = temp_model.from_map(m['StoryStartTimeRange'])
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')
        return self


class QueryStoriesShrinkRequest(TeaModel):
    def __init__(
        self,
        create_time_range_shrink: str = None,
        custom_labels: str = None,
        dataset_name: str = None,
        figure_cluster_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        story_end_time_range_shrink: str = None,
        story_name: str = None,
        story_start_time_range_shrink: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        with_empty_stories: bool = None,
    ):
        self.create_time_range_shrink = create_time_range_shrink
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        self.figure_cluster_ids_shrink = figure_cluster_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.object_id = object_id
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.sort = sort
        self.story_end_time_range_shrink = story_end_time_range_shrink
        self.story_name = story_name
        self.story_start_time_range_shrink = story_start_time_range_shrink
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.with_empty_stories = with_empty_stories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids_shrink is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.story_end_time_range_shrink is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range_shrink
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time_range_shrink is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range_shrink
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids_shrink = m.get('FigureClusterIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StoryEndTimeRange') is not None:
            self.story_end_time_range_shrink = m.get('StoryEndTimeRange')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTimeRange') is not None:
            self.story_start_time_range_shrink = m.get('StoryStartTimeRange')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')
        return self


class QueryStoriesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        stories: List[Story] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.stories = stories

    def validate(self):
        if self.stories:
            for k in self.stories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Stories'] = []
        if self.stories is not None:
            for k in self.stories:
                result['Stories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stories = []
        if m.get('Stories') is not None:
            for k in m.get('Stories'):
                temp_model = Story()
                self.stories.append(temp_model.from_map(k))
        return self


class QueryStoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryStoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebofficeTokenRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # This parameter is required.
        self.access_token = access_token
        self.credential_config = credential_config
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.refresh_token = refresh_token

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        credential_config_shrink: str = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # This parameter is required.
        self.access_token = access_token
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
        request_id: str = None,
    ):
        self.access_token = access_token
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token
        self.refresh_token_expired_time = refresh_token_expired_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshWebofficeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshWebofficeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveStoryFilesRequestFiles(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class RemoveStoryFilesRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[RemoveStoryFilesRequestFiles] = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files = files
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = RemoveStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class RemoveStoryFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.files_shrink = files_shrink
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class RemoveStoryFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveStoryFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveStoryFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeBatchRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ResumeBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeTriggerRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ResumeTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageFigureClusterRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        dataset_name: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class SearchImageFigureClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        dataset_name: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class SearchImageFigureClusterResponseBodyClusters(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        cluster_id: str = None,
        similarity: float = None,
    ):
        self.boundary = boundary
        self.cluster_id = cluster_id
        self.similarity = similarity

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        return self


class SearchImageFigureClusterResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[SearchImageFigureClusterResponseBodyClusters] = None,
        request_id: str = None,
    ):
        self.clusters = clusters
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = SearchImageFigureClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchImageFigureClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageFigureClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SemanticQueryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        media_types: List[str] = None,
        next_token: str = None,
        project_name: str = None,
        query: str = None,
        with_fields: List[str] = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.media_types = media_types
        self.next_token = next_token
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.query = query
        self.with_fields = with_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.media_types is not None:
            result['MediaTypes'] = self.media_types
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MediaTypes') is not None:
            self.media_types = m.get('MediaTypes')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class SemanticQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        media_types_shrink: str = None,
        next_token: str = None,
        project_name: str = None,
        query: str = None,
        with_fields_shrink: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.media_types_shrink = media_types_shrink
        self.next_token = next_token
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.query = query
        self.with_fields_shrink = with_fields_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.media_types_shrink is not None:
            result['MediaTypes'] = self.media_types_shrink
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MediaTypes') is not None:
            self.media_types_shrink = m.get('MediaTypes')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class SemanticQueryResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        request_id: str = None,
    ):
        self.files = files
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SemanticQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SemanticQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SemanticQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SimpleQueryRequestAggregations(TeaModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
    ):
        self.field = field
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class SimpleQueryRequest(TeaModel):
    def __init__(
        self,
        aggregations: List[SimpleQueryRequestAggregations] = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query: SimpleQuery = None,
        sort: str = None,
        with_fields: List[str] = None,
        without_total_hits: bool = None,
    ):
        self.aggregations = aggregations
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.query = query
        self.sort = sort
        self.with_fields = with_fields
        self.without_total_hits = without_total_hits

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query.to_map()
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        if self.without_total_hits is not None:
            result['WithoutTotalHits'] = self.without_total_hits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryRequestAggregations()
                self.aggregations.append(temp_model.from_map(k))
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            temp_model = SimpleQuery()
            self.query = temp_model.from_map(m['Query'])
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        if m.get('WithoutTotalHits') is not None:
            self.without_total_hits = m.get('WithoutTotalHits')
        return self


class SimpleQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregations_shrink: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query_shrink: str = None,
        sort: str = None,
        with_fields_shrink: str = None,
        without_total_hits: bool = None,
    ):
        self.aggregations_shrink = aggregations_shrink
        # This parameter is required.
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        # This parameter is required.
        self.project_name = project_name
        self.query_shrink = query_shrink
        self.sort = sort
        self.with_fields_shrink = with_fields_shrink
        self.without_total_hits = without_total_hits

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregations_shrink is not None:
            result['Aggregations'] = self.aggregations_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        if self.without_total_hits is not None:
            result['WithoutTotalHits'] = self.without_total_hits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            self.aggregations_shrink = m.get('Aggregations')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        if m.get('WithoutTotalHits') is not None:
            self.without_total_hits = m.get('WithoutTotalHits')
        return self


class SimpleQueryResponseBodyAggregationsGroups(TeaModel):
    def __init__(
        self,
        count: int = None,
        value: str = None,
    ):
        self.count = count
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SimpleQueryResponseBodyAggregations(TeaModel):
    def __init__(
        self,
        field: str = None,
        groups: List[SimpleQueryResponseBodyAggregationsGroups] = None,
        operation: str = None,
        value: float = None,
    ):
        self.field = field
        self.groups = groups
        self.operation = operation
        self.value = value

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = SimpleQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SimpleQueryResponseBody(TeaModel):
    def __init__(
        self,
        aggregations: List[SimpleQueryResponseBodyAggregations] = None,
        files: List[File] = None,
        next_token: str = None,
        request_id: str = None,
        total_hits: int = None,
    ):
        self.aggregations = aggregations
        self.files = files
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id
        self.total_hits = total_hits

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_hits is not None:
            result['TotalHits'] = self.total_hits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryResponseBodyAggregations()
                self.aggregations.append(temp_model.from_map(k))
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalHits') is not None:
            self.total_hits = m.get('TotalHits')
        return self


class SimpleQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SimpleQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SimpleQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendBatchRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class SuspendBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SuspendBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SuspendBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendTriggerRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class SuspendTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SuspendTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SuspendTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBatchRequestActions(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: List[str] = None,
    ):
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class UpdateBatchRequest(TeaModel):
    def __init__(
        self,
        actions: List[UpdateBatchRequestActions] = None,
        id: str = None,
        input: Input = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
    ):
        self.actions = actions
        # This parameter is required.
        self.id = id
        self.input = input
        # This parameter is required.
        self.project_name = project_name
        self.tags = tags

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = UpdateBatchRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateBatchShrinkRequest(TeaModel):
    def __init__(
        self,
        actions_shrink: str = None,
        id: str = None,
        input_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
    ):
        self.actions_shrink = actions_shrink
        # This parameter is required.
        self.id = id
        self.input_shrink = input_shrink
        # This parameter is required.
        self.project_name = project_name
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        project_name: str = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # This parameter is required.
        self.dataset_name = dataset_name
        self.description = description
        # This parameter is required.
        self.project_name = project_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset: Dataset = None,
        request_id: str = None,
    ):
        self.dataset = dataset
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFigureClusterRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        figure_cluster: FigureClusterForReq = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.figure_cluster = figure_cluster
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureCluster') is not None:
            temp_model = FigureClusterForReq()
            self.figure_cluster = temp_model.from_map(m['FigureCluster'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFigureClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        figure_cluster_shrink: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.figure_cluster_shrink = figure_cluster_shrink
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_shrink is not None:
            result['FigureCluster'] = self.figure_cluster_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureCluster') is not None:
            self.figure_cluster_shrink = m.get('FigureCluster')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFigureClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFigureClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFigureClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file: InputFile = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.file = file
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file is not None:
            result['File'] = self.file.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            temp_model = InputFile()
            self.file = temp_model.from_map(m['File'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file_shrink: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.file_shrink = file_shrink
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file_shrink is not None:
            result['File'] = self.file_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            self.file_shrink = m.get('File')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLocationDateClusterRequest(TeaModel):
    def __init__(
        self,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        title: str = None,
    ):
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateLocationDateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        title: str = None,
    ):
        self.custom_id = custom_id
        self.custom_labels_shrink = custom_labels_shrink
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateLocationDateClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLocationDateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLocationDateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLocationDateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        service_role: str = None,
        tag: List[UpdateProjectRequestTag] = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.description = description
        self.project_max_dataset_count = project_max_dataset_count
        # This parameter is required.
        self.project_name = project_name
        self.service_role = service_role
        self.tag = tag
        self.template_id = template_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateProjectRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        service_role: str = None,
        tag_shrink: str = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.description = description
        self.project_max_dataset_count = project_max_dataset_count
        # This parameter is required.
        self.project_name = project_name
        self.service_role = service_role
        self.tag_shrink = tag_shrink
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: Project = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoryRequestCover(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class UpdateStoryRequest(TeaModel):
    def __init__(
        self,
        cover: UpdateStoryRequestCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_name: str = None,
    ):
        self.cover = cover
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name
        self.story_name = story_name

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = UpdateStoryRequestCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        return self


class UpdateStoryShrinkRequest(TeaModel):
    def __init__(
        self,
        cover_shrink: str = None,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_name: str = None,
    ):
        self.cover_shrink = cover_shrink
        self.custom_id = custom_id
        self.custom_labels_shrink = custom_labels_shrink
        # This parameter is required.
        self.dataset_name = dataset_name
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.project_name = project_name
        self.story_name = story_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        return self


class UpdateStoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerRequestActions(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: List[str] = None,
    ):
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(
        self,
        actions: List[UpdateTriggerRequestActions] = None,
        id: str = None,
        input: Input = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
    ):
        self.actions = actions
        # This parameter is required.
        self.id = id
        self.input = input
        # This parameter is required.
        self.project_name = project_name
        self.tags = tags

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = UpdateTriggerRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateTriggerShrinkRequest(TeaModel):
    def __init__(
        self,
        actions_shrink: str = None,
        id: str = None,
        input_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
    ):
        self.actions_shrink = actions_shrink
        # This parameter is required.
        self.id = id
        self.input_shrink = input_shrink
        # This parameter is required.
        self.project_name = project_name
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


