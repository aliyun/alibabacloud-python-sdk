# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ExtraDataSourceMeta(TeaModel):
    def __init__(
        self,
        internal: bool = None,
        meta_type: str = None,
        project_name: str = None,
        table_name: str = None,
        type: str = None,
        update_frequency: int = None,
    ):
        self.internal = internal
        self.meta_type = meta_type
        self.project_name = project_name
        self.table_name = table_name
        self.type = type
        self.update_frequency = update_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.meta_type is not None:
            result['MetaType'] = self.meta_type
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('MetaType') is not None:
            self.meta_type = m.get('MetaType')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        return self


class ExtraDataSource(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ExtraDataSourceMeta = None,
        status: str = None,
        type: str = None,
    ):
        self.data_source_id = data_source_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.status = status
        self.type = type

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Meta') is not None:
            temp_model = ExtraDataSourceMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class FeatureTableMetaFeatureList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        feature_name: str = None,
        field_name: str = None,
        status: str = None,
    ):
        self.comment = comment
        self.feature_name = feature_name
        self.field_name = field_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FeatureTableMeta(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        feature_list: List[FeatureTableMetaFeatureList] = None,
        internal: bool = None,
        meta_type: str = None,
        source: str = None,
        update_frequency: int = None,
    ):
        self.data_source_id = data_source_id
        self.feature_list = feature_list
        self.internal = internal
        self.meta_type = meta_type
        self.source = source
        self.update_frequency = update_frequency

    def validate(self):
        if self.feature_list:
            for k in self.feature_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        result['FeatureList'] = []
        if self.feature_list is not None:
            for k in self.feature_list:
                result['FeatureList'].append(k.to_map() if k else None)
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.meta_type is not None:
            result['MetaType'] = self.meta_type
        if self.source is not None:
            result['Source'] = self.source
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        self.feature_list = []
        if m.get('FeatureList') is not None:
            for k in m.get('FeatureList'):
                temp_model = FeatureTableMetaFeatureList()
                self.feature_list.append(temp_model.from_map(k))
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('MetaType') is not None:
            self.meta_type = m.get('MetaType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        return self


class FeatureTable(TeaModel):
    def __init__(
        self,
        feature_table_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: FeatureTableMeta = None,
        status: str = None,
        type: str = None,
    ):
        self.feature_table_id = feature_table_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.status = status
        self.type = type

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_table_id is not None:
            result['FeatureTableId'] = self.feature_table_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureTableId') is not None:
            self.feature_table_id = m.get('FeatureTableId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Meta') is not None:
            temp_model = FeatureTableMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RankingModelTemplateMeta(TeaModel):
    def __init__(
        self,
        authorized: bool = None,
        auto_run: bool = None,
        auto_run_time: int = None,
        auto_run_type: str = None,
        can_deploy: bool = None,
        conf: str = None,
        deploy_status: str = None,
        last_edit_time: str = None,
        name: str = None,
        oss_arn: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        sample_id: str = None,
        sample_name: str = None,
        sample_time_window: int = None,
        sample_time_window_type: str = None,
        type: str = None,
    ):
        self.authorized = authorized
        self.auto_run = auto_run
        self.auto_run_time = auto_run_time
        self.auto_run_type = auto_run_type
        self.can_deploy = can_deploy
        self.conf = conf
        self.deploy_status = deploy_status
        self.last_edit_time = last_edit_time
        self.name = name
        self.oss_arn = oss_arn
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.sample_id = sample_id
        self.sample_name = sample_name
        self.sample_time_window = sample_time_window
        self.sample_time_window_type = sample_time_window_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.auto_run is not None:
            result['AutoRun'] = self.auto_run
        if self.auto_run_time is not None:
            result['AutoRunTime'] = self.auto_run_time
        if self.auto_run_type is not None:
            result['AutoRunType'] = self.auto_run_type
        if self.can_deploy is not None:
            result['CanDeploy'] = self.can_deploy
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_arn is not None:
            result['OssArn'] = self.oss_arn
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.sample_name is not None:
            result['SampleName'] = self.sample_name
        if self.sample_time_window is not None:
            result['SampleTimeWindow'] = self.sample_time_window
        if self.sample_time_window_type is not None:
            result['SampleTimeWindowType'] = self.sample_time_window_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('AutoRun') is not None:
            self.auto_run = m.get('AutoRun')
        if m.get('AutoRunTime') is not None:
            self.auto_run_time = m.get('AutoRunTime')
        if m.get('AutoRunType') is not None:
            self.auto_run_type = m.get('AutoRunType')
        if m.get('CanDeploy') is not None:
            self.can_deploy = m.get('CanDeploy')
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssArn') is not None:
            self.oss_arn = m.get('OssArn')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')
        if m.get('SampleTimeWindow') is not None:
            self.sample_time_window = m.get('SampleTimeWindow')
        if m.get('SampleTimeWindowType') is not None:
            self.sample_time_window_type = m.get('SampleTimeWindowType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RankingModelTemplate(TeaModel):
    def __init__(
        self,
        meta: RankingModelTemplateMeta = None,
        status: str = None,
        template_id: str = None,
        version_num: int = None,
    ):
        self.meta = meta
        self.status = status
        self.template_id = template_id
        self.version_num = version_num

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.version_num is not None:
            result['VersionNum'] = self.version_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = RankingModelTemplateMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('VersionNum') is not None:
            self.version_num = m.get('VersionNum')
        return self


class RankingModelVersionRunResult(TeaModel):
    def __init__(
        self,
        assess_auc: str = None,
        assess_gauc: str = None,
        assess_loss: str = None,
        train_auc: str = None,
        train_gauc: str = None,
        train_loss: str = None,
    ):
        self.assess_auc = assess_auc
        self.assess_gauc = assess_gauc
        self.assess_loss = assess_loss
        self.train_auc = train_auc
        self.train_gauc = train_gauc
        self.train_loss = train_loss

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assess_auc is not None:
            result['AssessAuc'] = self.assess_auc
        if self.assess_gauc is not None:
            result['AssessGauc'] = self.assess_gauc
        if self.assess_loss is not None:
            result['AssessLoss'] = self.assess_loss
        if self.train_auc is not None:
            result['TrainAuc'] = self.train_auc
        if self.train_gauc is not None:
            result['TrainGauc'] = self.train_gauc
        if self.train_loss is not None:
            result['TrainLoss'] = self.train_loss
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssessAuc') is not None:
            self.assess_auc = m.get('AssessAuc')
        if m.get('AssessGauc') is not None:
            self.assess_gauc = m.get('AssessGauc')
        if m.get('AssessLoss') is not None:
            self.assess_loss = m.get('AssessLoss')
        if m.get('TrainAuc') is not None:
            self.train_auc = m.get('TrainAuc')
        if m.get('TrainGauc') is not None:
            self.train_gauc = m.get('TrainGauc')
        if m.get('TrainLoss') is not None:
            self.train_loss = m.get('TrainLoss')
        return self


class RankingModelVersion(TeaModel):
    def __init__(
        self,
        name: str = None,
        run_log: str = None,
        run_result: RankingModelVersionRunResult = None,
        run_time: str = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        self.name = name
        self.run_log = run_log
        self.run_result = run_result
        self.run_time = run_time
        self.status = status
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        if self.run_result:
            self.run_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.run_log is not None:
            result['RunLog'] = self.run_log
        if self.run_result is not None:
            result['RunResult'] = self.run_result.to_map()
        if self.run_time is not None:
            result['RunTime'] = self.run_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RunLog') is not None:
            self.run_log = m.get('RunLog')
        if m.get('RunResult') is not None:
            temp_model = RankingModelVersionRunResult()
            self.run_result = temp_model.from_map(m['RunResult'])
        if m.get('RunTime') is not None:
            self.run_time = m.get('RunTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class RankingSystemMetaPredictEngine(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_id: str = None,
        version: str = None,
    ):
        self.cluster_id = cluster_id
        self.resource_id = resource_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class RankingSystemMeta(TeaModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        auto_deploy_auc: str = None,
        conf: str = None,
        fail_msg: str = None,
        model_version_name: str = None,
        predict_engine: RankingSystemMetaPredictEngine = None,
        predict_engine_type: str = None,
    ):
        self.auto_deploy = auto_deploy
        self.auto_deploy_auc = auto_deploy_auc
        self.conf = conf
        self.fail_msg = fail_msg
        self.model_version_name = model_version_name
        self.predict_engine = predict_engine
        self.predict_engine_type = predict_engine_type

    def validate(self):
        if self.predict_engine:
            self.predict_engine.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['AutoDeploy'] = self.auto_deploy
        if self.auto_deploy_auc is not None:
            result['AutoDeployAuc'] = self.auto_deploy_auc
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg
        if self.model_version_name is not None:
            result['ModelVersionName'] = self.model_version_name
        if self.predict_engine is not None:
            result['PredictEngine'] = self.predict_engine.to_map()
        if self.predict_engine_type is not None:
            result['PredictEngineType'] = self.predict_engine_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeploy') is not None:
            self.auto_deploy = m.get('AutoDeploy')
        if m.get('AutoDeployAuc') is not None:
            self.auto_deploy_auc = m.get('AutoDeployAuc')
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')
        if m.get('ModelVersionName') is not None:
            self.model_version_name = m.get('ModelVersionName')
        if m.get('PredictEngine') is not None:
            temp_model = RankingSystemMetaPredictEngine()
            self.predict_engine = temp_model.from_map(m['PredictEngine'])
        if m.get('PredictEngineType') is not None:
            self.predict_engine_type = m.get('PredictEngineType')
        return self


class RankingSystem(TeaModel):
    def __init__(
        self,
        apply_status: str = None,
        deploy_status: str = None,
        meta: RankingSystemMeta = None,
        model_template_id: str = None,
        name: str = None,
        scene_id_list: List[int] = None,
    ):
        self.apply_status = apply_status
        self.deploy_status = deploy_status
        self.meta = meta
        self.model_template_id = model_template_id
        self.name = name
        self.scene_id_list = scene_id_list

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status
        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id_list is not None:
            result['SceneIdList'] = self.scene_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')
        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')
        if m.get('Meta') is not None:
            temp_model = RankingSystemMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneIdList') is not None:
            self.scene_id_list = m.get('SceneIdList')
        return self


class RankingSystemHistoryMetaPredictEngine(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        version: str = None,
    ):
        self.resource_id = resource_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class RankingSystemHistoryMeta(TeaModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        auto_deploy_auc: str = None,
        conf: str = None,
        model_template_name: str = None,
        predict_engine: RankingSystemHistoryMetaPredictEngine = None,
        predict_engine_type: str = None,
        previous_operate_id: str = None,
    ):
        self.auto_deploy = auto_deploy
        self.auto_deploy_auc = auto_deploy_auc
        self.conf = conf
        self.model_template_name = model_template_name
        self.predict_engine = predict_engine
        self.predict_engine_type = predict_engine_type
        self.previous_operate_id = previous_operate_id

    def validate(self):
        if self.predict_engine:
            self.predict_engine.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['AutoDeploy'] = self.auto_deploy
        if self.auto_deploy_auc is not None:
            result['AutoDeployAuc'] = self.auto_deploy_auc
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.model_template_name is not None:
            result['ModelTemplateName'] = self.model_template_name
        if self.predict_engine is not None:
            result['PredictEngine'] = self.predict_engine.to_map()
        if self.predict_engine_type is not None:
            result['PredictEngineType'] = self.predict_engine_type
        if self.previous_operate_id is not None:
            result['PreviousOperateId'] = self.previous_operate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeploy') is not None:
            self.auto_deploy = m.get('AutoDeploy')
        if m.get('AutoDeployAuc') is not None:
            self.auto_deploy_auc = m.get('AutoDeployAuc')
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('ModelTemplateName') is not None:
            self.model_template_name = m.get('ModelTemplateName')
        if m.get('PredictEngine') is not None:
            temp_model = RankingSystemHistoryMetaPredictEngine()
            self.predict_engine = temp_model.from_map(m['PredictEngine'])
        if m.get('PredictEngineType') is not None:
            self.predict_engine_type = m.get('PredictEngineType')
        if m.get('PreviousOperateId') is not None:
            self.previous_operate_id = m.get('PreviousOperateId')
        return self


class RankingSystemHistory(TeaModel):
    def __init__(
        self,
        meta: RankingSystemHistoryMeta = None,
        name: str = None,
        operate_id: str = None,
        operate_time: str = None,
        operate_type: str = None,
    ):
        self.meta = meta
        self.name = name
        self.operate_id = operate_id
        self.operate_time = operate_time
        self.operate_type = operate_type

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_id is not None:
            result['OperateId'] = self.operate_id
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = RankingSystemHistoryMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateId') is not None:
            self.operate_id = m.get('OperateId')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class SampleMetaConfigFeatureConfig(TeaModel):
    def __init__(
        self,
        item_features: str = None,
        user_features: str = None,
    ):
        self.item_features = item_features
        self.user_features = user_features

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_features is not None:
            result['ItemFeatures'] = self.item_features
        if self.user_features is not None:
            result['UserFeatures'] = self.user_features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemFeatures') is not None:
            self.item_features = m.get('ItemFeatures')
        if m.get('UserFeatures') is not None:
            self.user_features = m.get('UserFeatures')
        return self


class SampleMetaConfigLabelLogic(TeaModel):
    def __init__(
        self,
        bhv_time_window: int = None,
        negative_bhv_types: str = None,
        positive_bhv_types: str = None,
    ):
        self.bhv_time_window = bhv_time_window
        self.negative_bhv_types = negative_bhv_types
        self.positive_bhv_types = positive_bhv_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bhv_time_window is not None:
            result['BhvTimeWindow'] = self.bhv_time_window
        if self.negative_bhv_types is not None:
            result['NegativeBhvTypes'] = self.negative_bhv_types
        if self.positive_bhv_types is not None:
            result['PositiveBhvTypes'] = self.positive_bhv_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BhvTimeWindow') is not None:
            self.bhv_time_window = m.get('BhvTimeWindow')
        if m.get('NegativeBhvTypes') is not None:
            self.negative_bhv_types = m.get('NegativeBhvTypes')
        if m.get('PositiveBhvTypes') is not None:
            self.positive_bhv_types = m.get('PositiveBhvTypes')
        return self


class SampleMetaConfigWeightLogicList(TeaModel):
    def __init__(
        self,
        bhv: str = None,
        weight: str = None,
    ):
        self.bhv = bhv
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bhv is not None:
            result['Bhv'] = self.bhv
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bhv') is not None:
            self.bhv = m.get('Bhv')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SampleMetaConfig(TeaModel):
    def __init__(
        self,
        bhv_table_source_ids: List[str] = None,
        feature_config: SampleMetaConfigFeatureConfig = None,
        label_logic: SampleMetaConfigLabelLogic = None,
        weight_logic_list: List[SampleMetaConfigWeightLogicList] = None,
    ):
        self.bhv_table_source_ids = bhv_table_source_ids
        self.feature_config = feature_config
        self.label_logic = label_logic
        self.weight_logic_list = weight_logic_list

    def validate(self):
        if self.feature_config:
            self.feature_config.validate()
        if self.label_logic:
            self.label_logic.validate()
        if self.weight_logic_list:
            for k in self.weight_logic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bhv_table_source_ids is not None:
            result['BhvTableSourceIds'] = self.bhv_table_source_ids
        if self.feature_config is not None:
            result['FeatureConfig'] = self.feature_config.to_map()
        if self.label_logic is not None:
            result['LabelLogic'] = self.label_logic.to_map()
        result['WeightLogicList'] = []
        if self.weight_logic_list is not None:
            for k in self.weight_logic_list:
                result['WeightLogicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BhvTableSourceIds') is not None:
            self.bhv_table_source_ids = m.get('BhvTableSourceIds')
        if m.get('FeatureConfig') is not None:
            temp_model = SampleMetaConfigFeatureConfig()
            self.feature_config = temp_model.from_map(m['FeatureConfig'])
        if m.get('LabelLogic') is not None:
            temp_model = SampleMetaConfigLabelLogic()
            self.label_logic = temp_model.from_map(m['LabelLogic'])
        self.weight_logic_list = []
        if m.get('WeightLogicList') is not None:
            for k in m.get('WeightLogicList'):
                temp_model = SampleMetaConfigWeightLogicList()
                self.weight_logic_list.append(temp_model.from_map(k))
        return self


class SampleMetaExtendParams(TeaModel):
    def __init__(
        self,
        latest_task_status: int = None,
        sample_count: int = None,
    ):
        self.latest_task_status = latest_task_status
        self.sample_count = sample_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_task_status is not None:
            result['LatestTaskStatus'] = self.latest_task_status
        if self.sample_count is not None:
            result['SampleCount'] = self.sample_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestTaskStatus') is not None:
            self.latest_task_status = m.get('LatestTaskStatus')
        if m.get('SampleCount') is not None:
            self.sample_count = m.get('SampleCount')
        return self


class SampleMeta(TeaModel):
    def __init__(
        self,
        auto_update: bool = None,
        auto_update_frequency: int = None,
        cloned_id: str = None,
        config: SampleMetaConfig = None,
        extend_params: SampleMetaExtendParams = None,
        meta_type: str = None,
        name: str = None,
        store_config: str = None,
        type: str = None,
    ):
        self.auto_update = auto_update
        self.auto_update_frequency = auto_update_frequency
        self.cloned_id = cloned_id
        self.config = config
        self.extend_params = extend_params
        self.meta_type = meta_type
        self.name = name
        self.store_config = store_config
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.extend_params:
            self.extend_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update
        if self.auto_update_frequency is not None:
            result['AutoUpdateFrequency'] = self.auto_update_frequency
        if self.cloned_id is not None:
            result['ClonedId'] = self.cloned_id
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.extend_params is not None:
            result['ExtendParams'] = self.extend_params.to_map()
        if self.meta_type is not None:
            result['MetaType'] = self.meta_type
        if self.name is not None:
            result['Name'] = self.name
        if self.store_config is not None:
            result['StoreConfig'] = self.store_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')
        if m.get('AutoUpdateFrequency') is not None:
            self.auto_update_frequency = m.get('AutoUpdateFrequency')
        if m.get('ClonedId') is not None:
            self.cloned_id = m.get('ClonedId')
        if m.get('Config') is not None:
            temp_model = SampleMetaConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExtendParams') is not None:
            temp_model = SampleMetaExtendParams()
            self.extend_params = temp_model.from_map(m['ExtendParams'])
        if m.get('MetaType') is not None:
            self.meta_type = m.get('MetaType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StoreConfig') is not None:
            self.store_config = m.get('StoreConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class Sample(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: SampleMeta = None,
        sample_id: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.sample_id = sample_id
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Meta') is not None:
            temp_model = SampleMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class AttachDatasetResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        state: str = None,
        version_id: str = None,
    ):
        # The time when the data source was created.
        self.gmt_create = gmt_create
        # The time when the data source was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the instance.
        self.instance_id = instance_id
        # The state for the dataset of the current version. Example: Importing. The value indicates that the dataset of the current version is being imported.
        self.state = state
        # The version number of the dataset.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.state is not None:
            result['state'] = self.state
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class AttachDatasetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: AttachDatasetResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The details about the dataset.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = AttachDatasetResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class AttachDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDatasetResponseBody = None,
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
            temp_model = AttachDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class AttachIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachIndexVersionResponseBody = None,
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
            temp_model = AttachIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRankingModelReachableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CheckRankingModelReachableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckRankingModelReachableResponseBody = None,
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
            temp_model = CheckRankingModelReachableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        # true: verifies experiment information. false (default): creates an experiment.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CloneExperimentResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        # The default value of the algorithm.
        self.default_value = default_value
        # The custom value of the algorithm.
        self.experiment_value = experiment_value
        # The algorithm key.
        self.key = key
        # The algorithm name. (Note: If you use the default algorithm, the console obtains the algorithm name from Medusa. If you customize an algorithm for the experiment, the algorithm name is directly returned.)
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CloneExperimentResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[CloneExperimentResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        # The algorithm category. Valid values: RECALL and RANK.
        self.category = category
        # The child configuration items.
        self.config = config
        # The default value of the algorithm configuration item.
        self.default_value = default_value
        # The custom value of the algorithm configuration item.
        self.experiment_value = experiment_value
        # Indicates whether child configuration items exist. Valid values: true and false.
        self.has_config = has_config
        # The algorithm key. Valid values: I2I: the I2I filtering algorithm. u2X2I: the U2X2I filtering algorithm. hot: the filtering algorithm for popular items. new: the filtering algorithm for new items. embedding: the vector filtering algorithm. mtorder: the priority of the filtering algorithm. rankservice: the ranking service.
        self.key = key
        # The algorithm name. (Note: If you use the default algorithm, the console obtains the algorithm name from Medusa. If you customize an algorithm for the experiment, the algorithm name is directly returned.)
        self.name = name
        # The algorithm type. Valid values: SYSTEM and CUSTOM.
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = CloneExperimentResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CloneExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithms: List[CloneExperimentResponseBodyResultAlgorithms] = None,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        # The algorithm configurations.
        self.algorithms = algorithms
        # N/A
        self.base = base
        # The buckets.
        self.buckets = buckets
        # The remarks.
        self.description = description
        # The experiment ID.
        self.experiment_id = experiment_id
        # The experiment name.
        self.name = name
        # The time when the experiment was unpublished.
        self.offline_time = offline_time
        # The time when the experiment was published.
        self.online_time = online_time
        # The experiment state.
        self.status = status

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = CloneExperimentResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CloneExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CloneExperimentResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the experiment.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CloneExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CloneExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneExperimentResponseBody = None,
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
            temp_model = CloneExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Sample = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = Sample()
            self.result = temp_model.from_map(m['result'])
        return self


class CloneSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneSampleResponseBody = None,
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
            temp_model = CloneSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ColdStartRankRequest(TeaModel):
    def __init__(
        self,
        features: str = None,
        imei: str = None,
        items: str = None,
        scene_id: str = None,
        user_id: str = None,
    ):
        self.features = features
        self.imei = imei
        self.items = items
        self.scene_id = scene_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.features is not None:
            result['features'] = self.features
        if self.imei is not None:
            result['imei'] = self.imei
        if self.items is not None:
            result['items'] = self.items
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('items') is not None:
            self.items = m.get('items')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ColdStartRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_type: str = None,
        trace_info: str = None,
    ):
        self.item_id = item_id
        self.item_type = item_type
        self.trace_info = trace_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.trace_info is not None:
            result['traceInfo'] = self.trace_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('traceInfo') is not None:
            self.trace_info = m.get('traceInfo')
        return self


class ColdStartRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ColdStartRankResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ColdStartRankResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ColdStartRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ColdStartRankResponseBody = None,
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
            temp_model = ColdStartRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateCustomAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateCustomAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomAnalysisTaskResponseBody = None,
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
            temp_model = CreateCustomAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Sample = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = Sample()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateCustomSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomSampleResponseBody = None,
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
            temp_model = CreateCustomSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataDiagnoseTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateDataDiagnoseTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataDiagnoseTaskResponseBody = None,
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
            temp_model = CreateDataDiagnoseTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExtraDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ExtraDataSource = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ExtraDataSource()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateExtraDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExtraDataSourceResponseBody = None,
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
            temp_model = CreateExtraDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFilteringAlgorithmRequest(TeaModel):
    def __init__(
        self,
        dry_run: str = None,
    ):
        # xxx
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        index_loss_threshold: int = None,
        index_size_threshold: int = None,
        source_data_record_threshold: int = None,
        source_data_size_threshold: int = None,
    ):
        # The time when the filtering table was modified.
        self.index_loss_threshold = index_loss_threshold
        # The fluctuation threshold for the size of the source table.
        self.index_size_threshold = index_size_threshold
        # The category of the filtering table.
        self.source_data_record_threshold = source_data_record_threshold
        # The fluctuation threshold for the loss of the index data.
        self.source_data_size_threshold = source_data_size_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        return self


class CreateFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        category: str = None,
        cron: str = None,
        cron_enabled: bool = None,
        description: str = None,
        ext_info: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        project_name: str = None,
        status: str = None,
        table_name: str = None,
        threshold: CreateFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        type: str = None,
    ):
        # The name of the filtering table.
        self.algorithm_name = algorithm_name
        # The response body.
        self.category = category
        # The fluctuation threshold for the size of the index.
        self.cron = cron
        # The time when the filtering table was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed UTC.
        self.cron_enabled = cron_enabled
        # The description of the filtering table.
        self.description = description
        # The name of the MaxCompute project.
        self.ext_info = ext_info
        # The information about the filtering table.
        self.gmt_create = gmt_create
        # Indicates whether the scheduled task is enabled.
        self.gmt_modified = gmt_modified
        # The ID of the filtering table.
        self.project_name = project_name
        # The CRON expression of the scheduled task. Example: 0 0/12 0 \\* \\*, which indicates that the task is scheduled at 00:00 and 12:00 every day.
        self.status = status
        # The metadata of the filtering table.
        self.table_name = table_name
        # 0 0/12 0 * *"
        self.threshold = threshold
        # The ID of the request.
        self.type = type

    def validate(self):
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.category is not None:
            result['category'] = self.category
        if self.cron is not None:
            result['cron'] = self.cron
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.status is not None:
            result['status'] = self.status
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('threshold') is not None:
            temp_model = CreateFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: CreateFilteringAlgorithmResponseBodyResultMeta = None,
        status: str = None,
    ):
        # The additional information.
        self.algorithm_id = algorithm_id
        # The time when the filtering table was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in Coordinated Universal Time (UTC).
        self.gmt_create = gmt_create
        # The fluctuation threshold for the data entries in the source table.
        self.gmt_modified = gmt_modified
        # The threshold.
        self.meta = meta
        # The name of the filtering algorithm.
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = CreateFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateFilteringAlgorithmResponseBodyResult = None,
    ):
        # The type of the data source.
        self.request_id = request_id
        # Specifies whether to perform a dry run. Valid values: true: performs a dry run. false: performs a dry run and sends the request.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFilteringAlgorithmResponseBody = None,
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
            temp_model = CreateFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowControlTaskRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFlowControlTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The time when the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the task was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in Coordinated Universal Time (UTC).
        self.gmt_modified = gmt_modified
        # The task state.
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateFlowControlTaskResponseBodyResult = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateFlowControlTaskResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowControlTaskResponseBody = None,
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
            temp_model = CreateFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateInstanceResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRankingModelRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: Dict[str, Any] = None,
        ranking_model_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.ranking_model_id = ranking_model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        return self


class CreateRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateRankingModelResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRankingModelResponseBody = None,
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
            temp_model = CreateRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRankingModelTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingModelTemplate = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingModelTemplate()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateRankingModelTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRankingModelTemplateResponseBody = None,
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
            temp_model = CreateRankingModelTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingSystem = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingSystem()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRankingSystemResponseBody = None,
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
            temp_model = CreateRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
        status: str = None,
    ):
        # The time when the rule was created.
        self.gmt_create = gmt_create
        # The time when the rule was last modified.
        self.gmt_modified = gmt_modified
        # The rule ID.
        self.rule_id = rule_id
        # Indicates whether the rule is enabled. Valid values: true and false.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateRuleResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRuleResponseBody = None,
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSampleFormatConfigRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateSampleFormatConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateSampleFormatConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSampleFormatConfigResponseBody = None,
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
            temp_model = CreateSampleFormatConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateSceneResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSceneResponseBody = None,
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
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUmengTokenRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # This parameter is required.
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CreateUmengTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateUmengTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUmengTokenResponseBody = None,
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
            temp_model = CreateUmengTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecribeRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: Dict[str, Any] = None,
        ranking_model_id: str = None,
    ):
        # The time when the ranking model was created.
        self.gmt_create = gmt_create
        # The time when the ranking model was last modified.
        self.gmt_modified = gmt_modified
        # The metadata.
        self.meta = meta
        # The ID of the ranking model.
        self.ranking_model_id = ranking_model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        return self


class DecribeRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DecribeRankingModelResponseBodyResult = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DecribeRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DecribeRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DecribeRankingModelResponseBody = None,
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
            temp_model = DecribeRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        state: str = None,
        version_id: str = None,
    ):
        # The time when the data source was created.
        self.gmt_create = gmt_create
        # The time when the data source was last modified.
        self.gmt_modified = gmt_modified
        # The instance ID.
        self.instance_id = instance_id
        # The state for the dataset of the current version. Example: Importing. The value indicates that the dataset of the current version is being imported.
        self.state = state
        # The version number of the dataset.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.state is not None:
            result['state'] = self.state
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class DeleteDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DeleteDataSetResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details about the dataset.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteDataSetResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSetResponseBody = None,
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
            temp_model = DeleteDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentResponseBody = None,
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
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExtraDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ExtraDataSource = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # 返回参数。
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ExtraDataSource()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteExtraDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExtraDataSourceResponseBody = None,
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
            temp_model = DeleteExtraDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilteringAlgorithmResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        item_separator: str = None,
        kv_separator: str = None,
    ):
        # The delimiter that is used to separate items.
        self.item_separator = item_separator
        # The delimiter that is used to separate keys and values.
        self.kv_separator = kv_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        return self


class DeleteFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        index_loss_threshold: int = None,
        index_size_threshold: int = None,
        source_data_record_threshold: int = None,
        source_data_size_threshold: int = None,
    ):
        # The fluctuation threshold for the loss of the index data.
        self.index_loss_threshold = index_loss_threshold
        # The fluctuation threshold for the size of the index.
        self.index_size_threshold = index_size_threshold
        # The fluctuation threshold for the data entries in the source table.
        self.source_data_record_threshold = source_data_record_threshold
        # The fluctuation threshold for the size of the source table.
        self.source_data_size_threshold = source_data_size_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        return self


class DeleteFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        category: str = None,
        cluster_id: str = None,
        cron: str = None,
        cron_enabled: bool = None,
        description: str = None,
        ext_info: DeleteFilteringAlgorithmResponseBodyResultMetaExtInfo = None,
        meta_type: str = None,
        project_name: str = None,
        table_name: str = None,
        task_id: str = None,
        threshold: DeleteFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        type: str = None,
    ):
        # The name of the filtering algorithm.
        self.algorithm_name = algorithm_name
        # The category of the filtering algorithm.
        self.category = category
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The CRON expression of the scheduled task. Example: 0 0/12 0 \\* \\*. The value indicates that the task is scheduled at 00:00 and 12:00 every day.
        self.cron = cron
        # N/A
        self.cron_enabled = cron_enabled
        # The description of the filtering table.
        self.description = description
        # The additional information.
        self.ext_info = ext_info
        # The type of the metadata.
        self.meta_type = meta_type
        # The name of the project.
        self.project_name = project_name
        # The name of the table.
        self.table_name = table_name
        # The ID of the task.
        self.task_id = task_id
        # The threshold.
        self.threshold = threshold
        # The type of the data source. Only MaxCompute is supported.
        self.type = type

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.category is not None:
            result['category'] = self.category
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extInfo') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('threshold') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DeleteFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: DeleteFilteringAlgorithmResponseBodyResultMeta = None,
        status: str = None,
    ):
        # The ID of the specified filtering table.
        self.algorithm_id = algorithm_id
        # The time when the filtering table was created.
        self.gmt_create = gmt_create
        # The time when the filtering table was modified.
        self.gmt_modified = gmt_modified
        # The metadata of the filtering table.
        self.meta = meta
        # The state of the filtering table. Valid values: Draft, Running, Offline, and Deleted.
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DeleteFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteFilteringAlgorithmResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFilteringAlgorithmResponseBody = None,
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
            temp_model = DeleteFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the task was deleted. Valid values: true and false.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowControlTaskResponseBody = None,
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
            temp_model = DeleteFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        ranking_model_id: str = None,
    ):
        # meta
        self.meta = meta
        self.ranking_model_id = ranking_model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['meta'] = self.meta
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        return self


class DeleteRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DeleteRankingModelResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRankingModelResponseBody = None,
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
            temp_model = DeleteRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRankingModelTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingModelTemplate = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingModelTemplate()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteRankingModelTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRankingModelTemplateResponseBody = None,
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
            temp_model = DeleteRankingModelTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRankingModelVersionResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRankingModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRankingModelVersionResponseBody = None,
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
            temp_model = DeleteRankingModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingSystem = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingSystem()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRankingSystemResponseBody = None,
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
            temp_model = DeleteRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Sample = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = Sample()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSampleResponseBody = None,
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
            temp_model = DeleteSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class DeleteSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DeleteSceneResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSceneResponseBody = None,
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
            temp_model = DeleteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployRankingSystemRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The schema of the response parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DeployRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The returned result.
        self.request_id = request_id
        # __null__
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeployRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployRankingSystemResponseBody = None,
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
            temp_model = DeployRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBaseExperimentResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.key = key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeBaseExperimentResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[DescribeBaseExperimentResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        self.category = category
        self.config = config
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.key = key
        self.name = name
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = DescribeBaseExperimentResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeBaseExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithms: List[DescribeBaseExperimentResponseBodyResultAlgorithms] = None,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        self.algorithms = algorithms
        self.base = base
        self.buckets = buckets
        self.description = description
        self.experiment_id = experiment_id
        self.name = name
        self.offline_time = offline_time
        self.online_time = online_time
        self.status = status

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = DescribeBaseExperimentResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeBaseExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeBaseExperimentResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeBaseExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeBaseExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBaseExperimentResponseBody = None,
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
            temp_model = DescribeBaseExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeCustomAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeCustomAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomAnalysisTaskResponseBody = None,
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
            temp_model = DescribeCustomAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSetMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        error_level: str = None,
        error_type: str = None,
        message: str = None,
        timestamp: str = None,
    ):
        self.error_level = error_level
        self.error_type = error_type
        self.message = message
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_level is not None:
            result['errorLevel'] = self.error_level
        if self.error_type is not None:
            result['errorType'] = self.error_type
        if self.message is not None:
            result['message'] = self.message
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLevel') is not None:
            self.error_level = m.get('errorLevel')
        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class DescribeDataSetMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeDataSetMessageResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeDataSetMessageResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeDataSetMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataSetMessageResponseBody = None,
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
            temp_model = DescribeDataSetMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefaultAlgorithmsResponseBodyResultConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        # The default value of the algorithm configuration item.
        self.default_value = default_value
        # The custom value of the algorithm configuration item.
        self.experiment_value = experiment_value
        # The key of the algorithm configuration item.
        self.key = key
        # The name of the algorithm configuration item. (Note: If you use the default algorithm, the console obtains the algorithm name from Medusa. If you customize an algorithm for the experiment, the algorithm name is directly returned.)
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeDefaultAlgorithmsResponseBodyResult(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[DescribeDefaultAlgorithmsResponseBodyResultConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        # The algorithm category. Valid values: RECALL and RANK.
        self.category = category
        # The information about the child configuration item.
        self.config = config
        # The default value of the algorithm. If you set key to i2i, hot, or new, the value of this parameter is true or false. If you set key to mtorder, the value of this parameter is a list of filtering algorithms ranked by priority.
        self.default_value = default_value
        # The custom value of the algorithm.
        self.experiment_value = experiment_value
        # Indicates whether child configuration items exist. Valid values: true and false.
        self.has_config = has_config
        # The algorithm key. Valid values: i2i: the I2I filtering algorithm. u2x2i: the U2X2I filtering algorithm. hot: the filtering algorithm for popular items. new: the filtering algorithm for new items. embedding: the vector filtering algorithm. mtorder: the priority of the filtering algorithm. rankservice: the ranking service.
        self.key = key
        # The algorithm name. (Note: If you use the default algorithm, the console obtains the algorithm name from Medusa. If you customize an algorithm for the experiment, the algorithm name is directly returned.)
        self.name = name
        # The algorithm type. Valid values: SYSTEM and CUSTOM.
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = DescribeDefaultAlgorithmsResponseBodyResultConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeDefaultAlgorithmsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeDefaultAlgorithmsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeDefaultAlgorithmsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeDefaultAlgorithmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDefaultAlgorithmsResponseBody = None,
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
            temp_model = DescribeDefaultAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExperimentResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        self.default_value = default_value
        self.experiment_value = experiment_value
        # key
        self.key = key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeExperimentResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[DescribeExperimentResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        # The category of the item.
        self.category = category
        self.config = config
        # None
        self.default_value = default_value
        # None
        self.experiment_value = experiment_value
        # None
        self.has_config = has_config
        # The key.
        self.key = key
        # The name of the experiment.
        self.name = name
        # None
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = DescribeExperimentResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithms: List[DescribeExperimentResponseBodyResultAlgorithms] = None,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        # The parameters about the experiment.
        self.algorithms = algorithms
        # None
        self.base = base
        self.buckets = buckets
        # The description of the experiment.
        self.description = description
        # The experiment ID.
        self.experiment_id = experiment_id
        # The name of the experiment.
        self.name = name
        # The time when the experiment was unpublished.
        self.offline_time = offline_time
        # The time when the experiment was published.
        self.online_time = online_time
        # The state of the experiment.
        self.status = status

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = DescribeExperimentResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeExperimentResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExperimentResponseBody = None,
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
            temp_model = DescribeExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExperimentEnvResponseBodyResult(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        divide_type: str = None,
    ):
        self.bucket_count = bucket_count
        self.divide_type = divide_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['bucketCount'] = self.bucket_count
        if self.divide_type is not None:
            result['divideType'] = self.divide_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketCount') is not None:
            self.bucket_count = m.get('bucketCount')
        if m.get('divideType') is not None:
            self.divide_type = m.get('divideType')
        return self


class DescribeExperimentEnvResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeExperimentEnvResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeExperimentEnvResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeExperimentEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExperimentEnvResponseBody = None,
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
            temp_model = DescribeExperimentEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExperimentEnvProgressResponseBodyResult(TeaModel):
    def __init__(
        self,
        progress: int = None,
        status: str = None,
    ):
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeExperimentEnvProgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeExperimentEnvProgressResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeExperimentEnvProgressResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeExperimentEnvProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExperimentEnvProgressResponseBody = None,
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
            temp_model = DescribeExperimentEnvProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFilteringAlgorithmResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        item_separator: str = None,
        kv_separator: str = None,
    ):
        # The description of the filtering table.
        self.item_separator = item_separator
        # The fluctuation threshold for the size of the index.
        self.kv_separator = kv_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        return self


class DescribeFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        index_loss_threshold: int = None,
        index_size_threshold: int = None,
        source_data_record_threshold: int = None,
        source_data_size_threshold: int = None,
    ):
        # The ID of the specified instance.
        self.index_loss_threshold = index_loss_threshold
        # Queries specific configuration information about a filtering table based on the ID of the filtering table.
        self.index_size_threshold = index_size_threshold
        # The type of the data source.
        self.source_data_record_threshold = source_data_record_threshold
        # The name of the filtering table.
        self.source_data_size_threshold = source_data_size_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        return self


class DescribeFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        category: str = None,
        cluster_id: str = None,
        cron: str = None,
        cron_enabled: bool = None,
        description: str = None,
        ext_info: DescribeFilteringAlgorithmResponseBodyResultMetaExtInfo = None,
        meta_type: str = None,
        project_name: str = None,
        table_name: str = None,
        task_id: str = None,
        threshold: DescribeFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        type: str = None,
    ):
        # The time when the filtering table was created.
        self.algorithm_name = algorithm_name
        # Indicates whether the scheduled task is enabled.
        self.category = category
        # N/A
        self.cluster_id = cluster_id
        # The information about the filtering table.
        self.cron = cron
        # The ID of the filtering table.
        self.cron_enabled = cron_enabled
        # The time when the filtering table was modified.
        self.description = description
        # The ID of the task.
        self.ext_info = ext_info
        # The information about the filtering table.
        self.meta_type = meta_type
        # The status of the filtering table.
        self.project_name = project_name
        # The ID of the specified filtering table.
        self.table_name = table_name
        # The CRON expression of the scheduled task.
        self.task_id = task_id
        # The ID of the filtering table.
        self.threshold = threshold
        # The metadata of the filtering table.
        self.type = type

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.category is not None:
            result['category'] = self.category
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extInfo') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('threshold') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: DescribeFilteringAlgorithmResponseBodyResultMeta = None,
        status: str = None,
    ):
        # The fluctuation threshold for the size of the source table.
        self.algorithm_id = algorithm_id
        # The category of the filtering table.
        self.gmt_create = gmt_create
        # The name of the project.
        self.gmt_modified = gmt_modified
        # The time when the filtering table was modified.
        self.meta = meta
        # N/A
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeFilteringAlgorithmResponseBodyResult = None,
    ):
        # The metadata of the filtering table.
        self.request_id = request_id
        # The ID of the request.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFilteringAlgorithmResponseBody = None,
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
            temp_model = DescribeFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        data_set_version: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        industry: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        name: str = None,
        region_id: str = None,
        scene: str = None,
        status: str = None,
        type: str = None,
    ):
        # The billing method. Valid values: PrePaid and PostPaid. Only the PrePaid billing method is supported.
        self.charge_type = charge_type
        # The commodity code of the recommended item.
        self.commodity_code = commodity_code
        # The version of the dataset that provides online services.
        self.data_set_version = data_set_version
        # The time when the instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.expired_time = expired_time
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the instance was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The type of the industry. Valid values: content, item, news, video, and sns.
        self.industry = industry
        # The instance ID.
        self.instance_id = instance_id
        # The lock mode of the instance. Valid values: Unlock, ManualLock, and LockByExpiration.
        self.lock_mode = lock_mode
        # The name of the instance.
        self.name = name
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The name of the scene. Valid values: gul, rr, hot, and focus.
        self.scene = scene
        # The state of the instance. Valid values: Initializing, Ready, and Running.
        self.status = status
        # The type of the instance. Only the Standard edition is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.data_set_version is not None:
            result['dataSetVersion'] = self.data_set_version
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.industry is not None:
            result['industry'] = self.industry
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.name is not None:
            result['name'] = self.name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.scene is not None:
            result['scene'] = self.scene
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('dataSetVersion') is not None:
            self.data_set_version = m.get('dataSetVersion')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeInstanceResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLatestTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        built_time: str = None,
        code: str = None,
        cost_seconds: int = None,
        flow_type: str = None,
        message: str = None,
        progress: int = None,
        rollback_enabled: bool = None,
        size: int = None,
        status: str = None,
        switched_time: str = None,
        version_id: str = None,
    ):
        self.built_time = built_time
        self.code = code
        self.cost_seconds = cost_seconds
        self.flow_type = flow_type
        self.message = message
        self.progress = progress
        self.rollback_enabled = rollback_enabled
        self.size = size
        self.status = status
        self.switched_time = switched_time
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.built_time is not None:
            result['builtTime'] = self.built_time
        if self.code is not None:
            result['code'] = self.code
        if self.cost_seconds is not None:
            result['costSeconds'] = self.cost_seconds
        if self.flow_type is not None:
            result['flowType'] = self.flow_type
        if self.message is not None:
            result['message'] = self.message
        if self.progress is not None:
            result['progress'] = self.progress
        if self.rollback_enabled is not None:
            result['rollbackEnabled'] = self.rollback_enabled
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('builtTime') is not None:
            self.built_time = m.get('builtTime')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('costSeconds') is not None:
            self.cost_seconds = m.get('costSeconds')
        if m.get('flowType') is not None:
            self.flow_type = m.get('flowType')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('rollbackEnabled') is not None:
            self.rollback_enabled = m.get('rollbackEnabled')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class DescribeLatestTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeLatestTaskResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeLatestTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeLatestTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLatestTaskResponseBody = None,
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
            temp_model = DescribeLatestTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQuotaResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_qps: int = None,
        item_count: int = None,
        item_count_used: int = None,
        qps: int = None,
        user_count: int = None,
        user_count_used: int = None,
    ):
        # The current QPS.
        self.current_qps = current_qps
        # The number of documents in the item table. Valid values:
        # 
        # 1000000 to 10000000.
        self.item_count = item_count
        # The number of items that are used in the item table.
        self.item_count_used = item_count_used
        # The queries per second (QPS). Valid values:
        # 
        # 10 to 500.
        self.qps = qps
        # The number of documents in the user table. Valid values:
        # 
        # 1000000 to 10000000.
        self.user_count = user_count
        # The number of users that are used in the user table.
        self.user_count_used = user_count_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_qps is not None:
            result['currentQps'] = self.current_qps
        if self.item_count is not None:
            result['itemCount'] = self.item_count
        if self.item_count_used is not None:
            result['itemCountUsed'] = self.item_count_used
        if self.qps is not None:
            result['qps'] = self.qps
        if self.user_count is not None:
            result['userCount'] = self.user_count
        if self.user_count_used is not None:
            result['userCountUsed'] = self.user_count_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentQps') is not None:
            self.current_qps = m.get('currentQps')
        if m.get('itemCount') is not None:
            self.item_count = m.get('itemCount')
        if m.get('itemCountUsed') is not None:
            self.item_count_used = m.get('itemCountUsed')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('userCount') is not None:
            self.user_count = m.get('userCount')
        if m.get('userCountUsed') is not None:
            self.user_count_used = m.get('userCountUsed')
        return self


class DescribeQuotaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeQuotaResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The quotas of the instance.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQuotaResponseBody = None,
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
            temp_model = DescribeQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The language of the response. Default value: zh-cn.
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        console_url: str = None,
        endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The console URL.
        self.console_url = console_url
        # The endpoint.
        self.endpoint = endpoint
        # The region name.
        self.local_name = local_name
        # The region ID of the instance.
        self.region_id = region_id
        # The instance state. Valid values: NotOpen, Processing, and Running.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_url is not None:
            result['consoleUrl'] = self.console_url
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleUrl') is not None:
            self.console_url = m.get('consoleUrl')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeRegionsResponseBodyResult] = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleRequest(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        scene_id: str = None,
    ):
        # The returned result.
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The type of the rule.
        # 
        # Valid values: selection and operation.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class DescribeRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.gmt_create = gmt_create
        # The state of the rule.
        self.gmt_modified = gmt_modified
        # The time when the rule was last modified.
        self.rule_id = rule_id
        # The time when the rule was created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeRuleResponseBodyResult = None,
    ):
        # The ID of the request.
        self.code = code
        # __null__
        self.message = message
        # The error message.
        self.request_id = request_id
        # The ID of the rule.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRuleResponseBody = None,
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
            temp_model = DescribeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeSceneResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSceneResponseBody = None,
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
            temp_model = DescribeSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneBucketResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: Dict[str, Any] = None,
        in_use: str = None,
        num: int = None,
    ):
        self.detail = detail
        self.in_use = in_use
        self.num = num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.in_use is not None:
            result['inUse'] = self.in_use
        if self.num is not None:
            result['num'] = self.num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('inUse') is not None:
            self.in_use = m.get('inUse')
        if m.get('num') is not None:
            self.num = m.get('num')
        return self


class DescribeSceneBucketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeSceneBucketResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSceneBucketResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSceneBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSceneBucketResponseBody = None,
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
            temp_model = DescribeSceneBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneThroughputResponseBodyResult(TeaModel):
    def __init__(
        self,
        pv_count: int = None,
    ):
        self.pv_count = pv_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pv_count is not None:
            result['pvCount'] = self.pv_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pvCount') is not None:
            self.pv_count = m.get('pvCount')
        return self


class DescribeSceneThroughputResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeSceneThroughputResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSceneThroughputResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSceneThroughputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSceneThroughputResponseBody = None,
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
            temp_model = DescribeSceneThroughputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncReportDetailRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        level_type: str = None,
        start_time: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.level_type = level_type
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.level_type is not None:
            result['levelType'] = self.level_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('levelType') is not None:
            self.level_type = m.get('levelType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeSyncReportDetailResponseBodyResultHistoryData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        error_percent: float = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.error_percent = error_percent
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.error_percent is not None:
            result['errorPercent'] = self.error_percent
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('errorPercent') is not None:
            self.error_percent = m.get('errorPercent')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class DescribeSyncReportDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        default_display: bool = None,
        error_count: int = None,
        error_percent: float = None,
        history_data: List[DescribeSyncReportDetailResponseBodyResultHistoryData] = None,
        sample_display: bool = None,
        type: str = None,
    ):
        self.default_display = default_display
        self.error_count = error_count
        self.error_percent = error_percent
        self.history_data = history_data
        self.sample_display = sample_display
        self.type = type

    def validate(self):
        if self.history_data:
            for k in self.history_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_display is not None:
            result['defaultDisplay'] = self.default_display
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_percent is not None:
            result['errorPercent'] = self.error_percent
        result['historyData'] = []
        if self.history_data is not None:
            for k in self.history_data:
                result['historyData'].append(k.to_map() if k else None)
        if self.sample_display is not None:
            result['sampleDisplay'] = self.sample_display
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultDisplay') is not None:
            self.default_display = m.get('defaultDisplay')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorPercent') is not None:
            self.error_percent = m.get('errorPercent')
        self.history_data = []
        if m.get('historyData') is not None:
            for k in m.get('historyData'):
                temp_model = DescribeSyncReportDetailResponseBodyResultHistoryData()
                self.history_data.append(temp_model.from_map(k))
        if m.get('sampleDisplay') is not None:
            self.sample_display = m.get('sampleDisplay')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeSyncReportDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeSyncReportDetailResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeSyncReportDetailResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeSyncReportDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSyncReportDetailResponseBody = None,
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
            temp_model = DescribeSyncReportDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncReportOutliersRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        key: str = None,
        level_type: str = None,
        start_time: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.level_type = level_type
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.key is not None:
            result['key'] = self.key
        if self.level_type is not None:
            result['levelType'] = self.level_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('levelType') is not None:
            self.level_type = m.get('levelType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeSyncReportOutliersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeSyncReportOutliersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSyncReportOutliersResponseBody = None,
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
            temp_model = DescribeSyncReportOutliersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserMetricsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        metric_type: str = None,
        start_time: int = None,
    ):
        # The end time. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of the user metric that you want to query. Valid values: pvCtr and uvCtr.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The start time. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class DescribeUserMetricsResponseBodyResultDataPoints(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        val: float = None,
    ):
        # The end time. The value is a timestamp in seconds.
        self.end_time = end_time
        # The start time. The value is a timestamp in seconds.
        self.start_time = start_time
        # The value of the corresponding metric.
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.val is not None:
            result['val'] = self.val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('val') is not None:
            self.val = m.get('val')
        return self


class DescribeUserMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_points: List[DescribeUserMetricsResponseBodyResultDataPoints] = None,
        scene_id: str = None,
    ):
        # The returned metrics.
        self.data_points = data_points
        # The scene ID.
        self.scene_id = scene_id

    def validate(self):
        if self.data_points:
            for k in self.data_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataPoints'] = []
        if self.data_points is not None:
            for k in self.data_points:
                result['dataPoints'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_points = []
        if m.get('dataPoints') is not None:
            for k in m.get('dataPoints'):
                temp_model = DescribeUserMetricsResponseBodyResultDataPoints()
                self.data_points.append(temp_model.from_map(k))
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class DescribeUserMetricsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeUserMetricsResponseBodyResult] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeUserMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeUserMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserMetricsResponseBody = None,
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
            temp_model = DescribeUserMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DowngradeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The new quota must be less than the selected quota.
        # 
        # The limits on the number of users: 1,000,000 to 10,000,000. The limits on the number of items: 1,000,000 to 10,000,000. The limits on the queries per second (QPS) of recommendation requests: 10 to 500.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DowngradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DowngradeInstanceResponseBodyResult = None,
    ):
        # The ID of the instance.
        self.code = code
        # The ID of the instance.
        self.message = message
        # The returned results.
        self.request_id = request_id
        # Decreases the quotas of a specified instance.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DowngradeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DowngradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DowngradeInstanceResponseBody = None,
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
            temp_model = DowngradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class EnableExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableExperimentResponseBody = None,
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
            temp_model = EnableExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Sample = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = Sample()
            self.result = temp_model.from_map(m['result'])
        return self


class GenerateSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateSampleResponseBody = None,
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
            temp_model = GenerateSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExtraDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ExtraDataSource = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ExtraDataSource()
            self.result = temp_model.from_map(m['result'])
        return self


class GetExtraDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExtraDataSourceResponseBody = None,
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
            temp_model = GetExtraDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowControlTaskResponseBodyResultMetaSelectionParams(TeaModel):
    def __init__(
        self,
        select_type: str = None,
        select_value: str = None,
        selection_operation: str = None,
    ):
        # The type of the filtering condition for the item selection rule.
        self.select_type = select_type
        # The value of the filtering condition for the item selection rule.
        self.select_value = select_value
        # The operation on the filtering condition for the item selection rule.
        self.selection_operation = selection_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_type is not None:
            result['selectType'] = self.select_type
        if self.select_value is not None:
            result['selectValue'] = self.select_value
        if self.selection_operation is not None:
            result['selectionOperation'] = self.selection_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        if m.get('selectValue') is not None:
            self.select_value = m.get('selectValue')
        if m.get('selectionOperation') is not None:
            self.selection_operation = m.get('selectionOperation')
        return self


class GetFlowControlTaskResponseBodyResultMetaTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        # EXPOSE_PERCENT: daily exposure percentage. EXPOSE_COUNT: total number of exposures.
        self.type = type
        # The exposure value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetFlowControlTaskResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        description: str = None,
        end_time: int = None,
        meta_type: str = None,
        scene_ids: str = None,
        selection_params: List[GetFlowControlTaskResponseBodyResultMetaSelectionParams] = None,
        start_time: int = None,
        target: GetFlowControlTaskResponseBodyResultMetaTarget = None,
        task_name: str = None,
    ):
        # The task description.
        self.description = description
        # The end time. The value is a timestamp in seconds.
        self.end_time = end_time
        # The metadata type.
        self.meta_type = meta_type
        # The scene IDs.
        self.scene_ids = scene_ids
        # The parameters specified for the item selection rule.
        self.selection_params = selection_params
        # The start time. The value is a timestamp in seconds.
        self.start_time = start_time
        # The exposure settings.
        self.target = target
        # The task name.
        self.task_name = task_name

    def validate(self):
        if self.selection_params:
            for k in self.selection_params:
                if k:
                    k.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        result['selectionParams'] = []
        if self.selection_params is not None:
            for k in self.selection_params:
                result['selectionParams'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        self.selection_params = []
        if m.get('selectionParams') is not None:
            for k in m.get('selectionParams'):
                temp_model = GetFlowControlTaskResponseBodyResultMetaSelectionParams()
                self.selection_params.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            temp_model = GetFlowControlTaskResponseBodyResultMetaTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class GetFlowControlTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: GetFlowControlTaskResponseBodyResultMeta = None,
        status: str = None,
        task_id: str = None,
    ):
        # The time when the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in Coordinated Universal Time (UTC).
        self.gmt_create = gmt_create
        # The time when the data source was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The metadata of the task.
        self.meta = meta
        # The task state. Valid values: DRAFT, READY, RUNNING, ENDED, and AUTO_END. The value AUTO_END is not used.
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = GetFlowControlTaskResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetFlowControlTaskResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetFlowControlTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowControlTaskResponseBody = None,
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
            temp_model = GetFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestDataDiagnoseTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetLatestDataDiagnoseTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLatestDataDiagnoseTaskStatusResponseBody = None,
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
            temp_model = GetLatestDataDiagnoseTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRankingModelTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingModelTemplate = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingModelTemplate()
            self.result = temp_model.from_map(m['result'])
        return self


class GetRankingModelTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRankingModelTemplateResponseBody = None,
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
            temp_model = GetRankingModelTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRankingModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingModelVersion = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingModelVersion()
            self.result = temp_model.from_map(m['result'])
        return self


class GetRankingModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRankingModelVersionResponseBody = None,
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
            temp_model = GetRankingModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingSystem = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingSystem()
            self.result = temp_model.from_map(m['result'])
        return self


class GetRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRankingSystemResponseBody = None,
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
            temp_model = GetRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRankingSystemHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingSystemHistory = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingSystemHistory()
            self.result = temp_model.from_map(m['result'])
        return self


class GetRankingSystemHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRankingSystemHistoryResponseBody = None,
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
            temp_model = GetRankingSystemHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSampleRequest(TeaModel):
    def __init__(
        self,
        with_extend_parmas: bool = None,
    ):
        self.with_extend_parmas = with_extend_parmas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_extend_parmas is not None:
            result['withExtendParmas'] = self.with_extend_parmas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withExtendParmas') is not None:
            self.with_extend_parmas = m.get('withExtendParmas')
        return self


class GetSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Sample = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = Sample()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSampleResponseBody = None,
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
            temp_model = GetSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitComputingResourceRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
    ):
        self.key = key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InitComputingResourceResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class InitComputingResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitComputingResourceResponseBody = None,
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
            temp_model = InitComputingResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardDetailsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        experiment_ids: str = None,
        match_types: str = None,
        metric_type: str = None,
        scene_ids: str = None,
        start_time: int = None,
        trace_ids: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.experiment_ids = experiment_ids
        self.match_types = match_types
        # This parameter is required.
        self.metric_type = metric_type
        # This parameter is required.
        self.scene_ids = scene_ids
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.trace_ids = trace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.experiment_ids is not None:
            result['experimentIds'] = self.experiment_ids
        if self.match_types is not None:
            result['matchTypes'] = self.match_types
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.trace_ids is not None:
            result['traceIds'] = self.trace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('experimentIds') is not None:
            self.experiment_ids = m.get('experimentIds')
        if m.get('matchTypes') is not None:
            self.match_types = m.get('matchTypes')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('traceIds') is not None:
            self.trace_ids = m.get('traceIds')
        return self


class ListDashboardDetailsResponseBodyResultMetricRes(TeaModel):
    def __init__(
        self,
        detail: Dict[str, Any] = None,
        total: Dict[str, Any] = None,
    ):
        self.detail = detail
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDashboardDetailsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_res: ListDashboardDetailsResponseBodyResultMetricRes = None,
        scene_id: str = None,
        trace_id: str = None,
    ):
        self.metric_res = metric_res
        self.scene_id = scene_id
        self.trace_id = trace_id

    def validate(self):
        if self.metric_res:
            self.metric_res.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_res is not None:
            result['metricRes'] = self.metric_res.to_map()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricRes') is not None:
            temp_model = ListDashboardDetailsResponseBodyResultMetricRes()
            self.metric_res = temp_model.from_map(m['metricRes'])
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ListDashboardDetailsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDashboardDetailsResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDashboardDetailsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDashboardDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDashboardDetailsResponseBody = None,
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
            temp_model = ListDashboardDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardDetailsFlowsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        experiment_ids: str = None,
        metric_type: str = None,
        scene_ids: str = None,
        start_time: int = None,
        trace_ids: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.experiment_ids = experiment_ids
        # This parameter is required.
        self.metric_type = metric_type
        # This parameter is required.
        self.scene_ids = scene_ids
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.trace_ids = trace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.experiment_ids is not None:
            result['experimentIds'] = self.experiment_ids
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.trace_ids is not None:
            result['traceIds'] = self.trace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('experimentIds') is not None:
            self.experiment_ids = m.get('experimentIds')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('traceIds') is not None:
            self.trace_ids = m.get('traceIds')
        return self


class ListDashboardDetailsFlowsResponseBodyResultMetricData(TeaModel):
    def __init__(
        self,
        metric_res: Dict[str, Any] = None,
        scene_id: str = None,
        trace_id: str = None,
    ):
        self.metric_res = metric_res
        self.scene_id = scene_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_res is not None:
            result['metricRes'] = self.metric_res
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricRes') is not None:
            self.metric_res = m.get('metricRes')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ListDashboardDetailsFlowsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_data: List[ListDashboardDetailsFlowsResponseBodyResultMetricData] = None,
        metric_type: str = None,
    ):
        self.metric_data = metric_data
        self.metric_type = metric_type

    def validate(self):
        if self.metric_data:
            for k in self.metric_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['metricData'] = []
        if self.metric_data is not None:
            for k in self.metric_data:
                result['metricData'].append(k.to_map() if k else None)
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_data = []
        if m.get('metricData') is not None:
            for k in m.get('metricData'):
                temp_model = ListDashboardDetailsFlowsResponseBodyResultMetricData()
                self.metric_data.append(temp_model.from_map(k))
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        return self


class ListDashboardDetailsFlowsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ListDashboardDetailsFlowsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListDashboardDetailsFlowsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListDashboardDetailsFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDashboardDetailsFlowsResponseBody = None,
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
            temp_model = ListDashboardDetailsFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardMetricsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        metric_query: str = None,
        metric_type: str = None,
        metric_view: str = None,
        start_time: int = None,
    ):
        # The statistical results.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.metric_query = metric_query
        # The statistical results.
        self.metric_type = metric_type
        self.metric_view = metric_view
        # USERACTIONPV_COUNT
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.metric_query is not None:
            result['metricQuery'] = self.metric_query
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.metric_view is not None:
            result['metricView'] = self.metric_view
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metricQuery') is not None:
            self.metric_query = m.get('metricQuery')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('metricView') is not None:
            self.metric_view = m.get('metricView')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListDashboardMetricsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        val: str = None,
    ):
        # The error message.
        self.end_time = end_time
        # The ID of the request.
        self.start_time = start_time
        # The error code.
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.val is not None:
            result['val'] = self.val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('val') is not None:
            self.val = m.get('val')
        return self


class ListDashboardMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: List[ListDashboardMetricsResponseBodyResultDetail] = None,
        total: Dict[str, Any] = None,
    ):
        # The end time. The value is a timestamp in seconds.
        self.detail = detail
        # The start time. The value is a timestamp in seconds.
        self.total = total

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListDashboardMetricsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDashboardMetricsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDashboardMetricsResponseBodyResult] = None,
    ):
        # __null__
        self.code = code
        self.message = message
        self.request_id = request_id
        # The specific value of the metric.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDashboardMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDashboardMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDashboardMetricsResponseBody = None,
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
            temp_model = ListDashboardMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardMetricsFlowsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        metric_type: str = None,
        start_time: int = None,
    ):
        # The type of the metric.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The metric data.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The statistical results.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListDashboardMetricsFlowsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_data: Dict[str, Any] = None,
        metric_type: str = None,
    ):
        # __null__
        self.metric_data = metric_data
        # The error message.
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_data is not None:
            result['metricData'] = self.metric_data
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricData') is not None:
            self.metric_data = m.get('metricData')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        return self


class ListDashboardMetricsFlowsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDashboardMetricsFlowsResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        # The ID of the request.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDashboardMetricsFlowsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDashboardMetricsFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDashboardMetricsFlowsResponseBody = None,
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
            temp_model = ListDashboardMetricsFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataDiagnoseReportsRequest(TeaModel):
    def __init__(
        self,
        task_create_time: int = None,
    ):
        self.task_create_time = task_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_create_time is not None:
            result['taskCreateTime'] = self.task_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskCreateTime') is not None:
            self.task_create_time = m.get('taskCreateTime')
        return self


class ListDataDiagnoseReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListDataDiagnoseReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataDiagnoseReportsResponseBody = None,
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
            temp_model = ListDataDiagnoseReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataDiagnoseSampleDetailsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        key: str = None,
        start_time: int = None,
        task_create_time: int = None,
        task_source: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.task_create_time = task_create_time
        # This parameter is required.
        self.task_source = task_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.key is not None:
            result['key'] = self.key
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_create_time is not None:
            result['taskCreateTime'] = self.task_create_time
        if self.task_source is not None:
            result['taskSource'] = self.task_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskCreateTime') is not None:
            self.task_create_time = m.get('taskCreateTime')
        if m.get('taskSource') is not None:
            self.task_source = m.get('taskSource')
        return self


class ListDataDiagnoseSampleDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListDataDiagnoseSampleDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataDiagnoseSampleDetailsResponseBody = None,
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
            temp_model = ListDataDiagnoseSampleDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        state: str = None,
        version_id: str = None,
    ):
        # The time when the data source was created.
        self.gmt_create = gmt_create
        # The time when the data source was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the instance.
        self.instance_id = instance_id
        # The state for the dataset of the current version. Example: Importing. The value indicates that the dataset of the current version is being imported.
        self.state = state
        # The version number of the dataset.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.state is not None:
            result['state'] = self.state
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDataSetResponseBodyResult] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned datasets.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSetResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSetResponseBody = None,
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
            temp_model = ListDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket_name: str = None,
        partition: str = None,
        path: str = None,
        project_name: str = None,
        table_name: str = None,
        timestamp: int = None,
        type: str = None,
    ):
        self.access_key_id = access_key_id
        self.bucket_name = bucket_name
        self.partition = partition
        self.path = path
        self.project_name = project_name
        self.table_name = table_name
        self.timestamp = timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ListDataSourceResponseBodyResultMeta = None,
        table_name: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.table_name = table_name

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ListDataSourceResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class ListDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDataSourceResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceResponseBody = None,
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
            temp_model = ListDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        self.base = base
        self.buckets = buckets
        self.description = description
        self.experiment_id = experiment_id
        self.name = name
        self.offline_time = offline_time
        self.online_time = online_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListExperimentsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListExperimentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentsResponseBody = None,
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
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExtraDataSourcesRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListExtraDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ExtraDataSource] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ExtraDataSource()
                self.result.append(temp_model.from_map(k))
        return self


class ListExtraDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExtraDataSourcesResponseBody = None,
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
            temp_model = ListExtraDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureTablesRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        type: str = None,
        update_frequency: str = None,
    ):
        self.data_source_id = data_source_id
        self.type = type
        self.update_frequency = update_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.type is not None:
            result['type'] = self.type
        if self.update_frequency is not None:
            result['updateFrequency'] = self.update_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateFrequency') is not None:
            self.update_frequency = m.get('updateFrequency')
        return self


class ListFeatureTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[FeatureTable] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = FeatureTable()
                self.result.append(temp_model.from_map(k))
        return self


class ListFeatureTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureTablesResponseBody = None,
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
            temp_model = ListFeatureTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFilteringAlgorithmsRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        page: int = None,
        size: int = None,
        status: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.page = page
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListFilteringAlgorithmsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListFilteringAlgorithmsResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        item_separator: str = None,
        kv_separator: str = None,
    ):
        self.item_separator = item_separator
        self.kv_separator = kv_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        return self


class ListFilteringAlgorithmsResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        index_loss_threshold: int = None,
        index_size_threshold: int = None,
        source_data_record_threshold: int = None,
        source_data_size_threshold: int = None,
    ):
        self.index_loss_threshold = index_loss_threshold
        self.index_size_threshold = index_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.source_data_size_threshold = source_data_size_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        return self


class ListFilteringAlgorithmsResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        category: str = None,
        cluster_id: str = None,
        cron: str = None,
        cron_enabled: bool = None,
        description: str = None,
        ext_info: ListFilteringAlgorithmsResponseBodyResultMetaExtInfo = None,
        meta_type: str = None,
        project_name: str = None,
        table_name: str = None,
        task_id: str = None,
        threshold: ListFilteringAlgorithmsResponseBodyResultMetaThreshold = None,
        type: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.category = category
        self.cluster_id = cluster_id
        self.cron = cron
        self.cron_enabled = cron_enabled
        self.description = description
        self.ext_info = ext_info
        self.meta_type = meta_type
        self.project_name = project_name
        self.table_name = table_name
        self.task_id = task_id
        self.threshold = threshold
        self.type = type

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.category is not None:
            result['category'] = self.category
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extInfo') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('threshold') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListFilteringAlgorithmsResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ListFilteringAlgorithmsResponseBodyResultMeta = None,
        status: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListFilteringAlgorithmsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListFilteringAlgorithmsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListFilteringAlgorithmsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['headers'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFilteringAlgorithmsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListFilteringAlgorithmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFilteringAlgorithmsResponseBody = None,
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
            temp_model = ListFilteringAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowControlTaskRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        status: str = None,
        task_id: str = None,
    ):
        self.page = page
        self.size = size
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListFlowControlTaskResponseBodyResultMetaSelectionParams(TeaModel):
    def __init__(
        self,
        select_type: str = None,
        select_value: str = None,
        selection_operation: str = None,
    ):
        self.select_type = select_type
        self.select_value = select_value
        self.selection_operation = selection_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_type is not None:
            result['selectType'] = self.select_type
        if self.select_value is not None:
            result['selectValue'] = self.select_value
        if self.selection_operation is not None:
            result['selectionOperation'] = self.selection_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        if m.get('selectValue') is not None:
            self.select_value = m.get('selectValue')
        if m.get('selectionOperation') is not None:
            self.selection_operation = m.get('selectionOperation')
        return self


class ListFlowControlTaskResponseBodyResultMetaTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListFlowControlTaskResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        description: str = None,
        end_time: int = None,
        meta_type: str = None,
        scene_ids: str = None,
        selection_params: List[ListFlowControlTaskResponseBodyResultMetaSelectionParams] = None,
        start_time: int = None,
        target: ListFlowControlTaskResponseBodyResultMetaTarget = None,
        task_name: str = None,
    ):
        self.description = description
        self.end_time = end_time
        self.meta_type = meta_type
        self.scene_ids = scene_ids
        self.selection_params = selection_params
        self.start_time = start_time
        self.target = target
        self.task_name = task_name

    def validate(self):
        if self.selection_params:
            for k in self.selection_params:
                if k:
                    k.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        result['selectionParams'] = []
        if self.selection_params is not None:
            for k in self.selection_params:
                result['selectionParams'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        self.selection_params = []
        if m.get('selectionParams') is not None:
            for k in m.get('selectionParams'):
                temp_model = ListFlowControlTaskResponseBodyResultMetaSelectionParams()
                self.selection_params.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            temp_model = ListFlowControlTaskResponseBodyResultMetaTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class ListFlowControlTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ListFlowControlTaskResponseBodyResultMeta = None,
        status: str = None,
    ):
        self.task_id = task_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ListFlowControlTaskResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListFlowControlTaskResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFlowControlTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowControlTaskResponseBody = None,
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
            temp_model = ListFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowControlTaskInvalidItemsRequest(TeaModel):
    def __init__(
        self,
        body: List[str] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ListFlowControlTaskInvalidItemsResponseBodyResultInvalidItems(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_type: str = None,
    ):
        self.item_id = item_id
        self.item_type = item_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        return self


class ListFlowControlTaskInvalidItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        invalid_items: List[ListFlowControlTaskInvalidItemsResponseBodyResultInvalidItems] = None,
    ):
        self.invalid_items = invalid_items

    def validate(self):
        if self.invalid_items:
            for k in self.invalid_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['invalidItems'] = []
        if self.invalid_items is not None:
            for k in self.invalid_items:
                result['invalidItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invalid_items = []
        if m.get('invalidItems') is not None:
            for k in m.get('invalidItems'):
                temp_model = ListFlowControlTaskInvalidItemsResponseBodyResultInvalidItems()
                self.invalid_items.append(temp_model.from_map(k))
        return self


class ListFlowControlTaskInvalidItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListFlowControlTaskInvalidItemsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFlowControlTaskInvalidItemsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListFlowControlTaskInvalidItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowControlTaskInvalidItemsResponseBody = None,
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
            temp_model = ListFlowControlTaskInvalidItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowControlTaskItemReportsRequest(TeaModel):
    def __init__(
        self,
        count: str = None,
        select_time_type: str = None,
        select_type: str = None,
    ):
        self.count = count
        self.select_time_type = select_time_type
        self.select_type = select_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.select_time_type is not None:
            result['selectTimeType'] = self.select_time_type
        if self.select_type is not None:
            result['selectType'] = self.select_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('selectTimeType') is not None:
            self.select_time_type = m.get('selectTimeType')
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        return self


class ListFlowControlTaskItemReportsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        acc_click_percent: str = None,
        acc_item_click: str = None,
        acc_item_ctr: str = None,
        acc_item_pv: str = None,
        acc_pv_percent: str = None,
        acc_task_click: str = None,
        acc_task_ctr: str = None,
        acc_task_pv: str = None,
        acc_task_rank: str = None,
        click_percent: str = None,
        item_click: str = None,
        item_ctr: str = None,
        item_id: str = None,
        item_pv: str = None,
        item_type: str = None,
        pv_percent: str = None,
        task_click: str = None,
        task_ctr: str = None,
        task_id: str = None,
        task_pv: str = None,
        task_rank: str = None,
    ):
        self.acc_click_percent = acc_click_percent
        self.acc_item_click = acc_item_click
        self.acc_item_ctr = acc_item_ctr
        self.acc_item_pv = acc_item_pv
        self.acc_pv_percent = acc_pv_percent
        self.acc_task_click = acc_task_click
        self.acc_task_ctr = acc_task_ctr
        self.acc_task_pv = acc_task_pv
        self.acc_task_rank = acc_task_rank
        self.click_percent = click_percent
        self.item_click = item_click
        self.item_ctr = item_ctr
        self.item_id = item_id
        self.item_pv = item_pv
        self.item_type = item_type
        self.pv_percent = pv_percent
        self.task_click = task_click
        self.task_ctr = task_ctr
        self.task_id = task_id
        self.task_pv = task_pv
        self.task_rank = task_rank

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc_click_percent is not None:
            result['accClickPercent'] = self.acc_click_percent
        if self.acc_item_click is not None:
            result['accItemClick'] = self.acc_item_click
        if self.acc_item_ctr is not None:
            result['accItemCtr'] = self.acc_item_ctr
        if self.acc_item_pv is not None:
            result['accItemPv'] = self.acc_item_pv
        if self.acc_pv_percent is not None:
            result['accPvPercent'] = self.acc_pv_percent
        if self.acc_task_click is not None:
            result['accTaskClick'] = self.acc_task_click
        if self.acc_task_ctr is not None:
            result['accTaskCtr'] = self.acc_task_ctr
        if self.acc_task_pv is not None:
            result['accTaskPv'] = self.acc_task_pv
        if self.acc_task_rank is not None:
            result['accTaskRank'] = self.acc_task_rank
        if self.click_percent is not None:
            result['clickPercent'] = self.click_percent
        if self.item_click is not None:
            result['itemClick'] = self.item_click
        if self.item_ctr is not None:
            result['itemCtr'] = self.item_ctr
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_pv is not None:
            result['itemPv'] = self.item_pv
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.pv_percent is not None:
            result['pvPercent'] = self.pv_percent
        if self.task_click is not None:
            result['taskClick'] = self.task_click
        if self.task_ctr is not None:
            result['taskCtr'] = self.task_ctr
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_pv is not None:
            result['taskPv'] = self.task_pv
        if self.task_rank is not None:
            result['taskRank'] = self.task_rank
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accClickPercent') is not None:
            self.acc_click_percent = m.get('accClickPercent')
        if m.get('accItemClick') is not None:
            self.acc_item_click = m.get('accItemClick')
        if m.get('accItemCtr') is not None:
            self.acc_item_ctr = m.get('accItemCtr')
        if m.get('accItemPv') is not None:
            self.acc_item_pv = m.get('accItemPv')
        if m.get('accPvPercent') is not None:
            self.acc_pv_percent = m.get('accPvPercent')
        if m.get('accTaskClick') is not None:
            self.acc_task_click = m.get('accTaskClick')
        if m.get('accTaskCtr') is not None:
            self.acc_task_ctr = m.get('accTaskCtr')
        if m.get('accTaskPv') is not None:
            self.acc_task_pv = m.get('accTaskPv')
        if m.get('accTaskRank') is not None:
            self.acc_task_rank = m.get('accTaskRank')
        if m.get('clickPercent') is not None:
            self.click_percent = m.get('clickPercent')
        if m.get('itemClick') is not None:
            self.item_click = m.get('itemClick')
        if m.get('itemCtr') is not None:
            self.item_ctr = m.get('itemCtr')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemPv') is not None:
            self.item_pv = m.get('itemPv')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('pvPercent') is not None:
            self.pv_percent = m.get('pvPercent')
        if m.get('taskClick') is not None:
            self.task_click = m.get('taskClick')
        if m.get('taskCtr') is not None:
            self.task_ctr = m.get('taskCtr')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskPv') is not None:
            self.task_pv = m.get('taskPv')
        if m.get('taskRank') is not None:
            self.task_rank = m.get('taskRank')
        return self


class ListFlowControlTaskItemReportsResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: List[ListFlowControlTaskItemReportsResponseBodyResultDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListFlowControlTaskItemReportsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListFlowControlTaskItemReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListFlowControlTaskItemReportsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListFlowControlTaskItemReportsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListFlowControlTaskItemReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowControlTaskItemReportsResponseBody = None,
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
            temp_model = ListFlowControlTaskItemReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowControlTaskItemsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListFlowControlTaskItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        author: str = None,
        category_path: str = None,
        channel: str = None,
        duration: str = None,
        expire_time: str = None,
        item_id: str = None,
        item_type: str = None,
        last_modify_time: str = None,
        pub_time: str = None,
        status: str = None,
        title: str = None,
        weight: str = None,
    ):
        self.author = author
        self.category_path = category_path
        self.channel = channel
        self.duration = duration
        self.expire_time = expire_time
        self.item_id = item_id
        self.item_type = item_type
        self.last_modify_time = last_modify_time
        self.pub_time = pub_time
        self.status = status
        self.title = title
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['author'] = self.author
        if self.category_path is not None:
            result['categoryPath'] = self.category_path
        if self.channel is not None:
            result['channel'] = self.channel
        if self.duration is not None:
            result['duration'] = self.duration
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.status is not None:
            result['status'] = self.status
        if self.title is not None:
            result['title'] = self.title
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('categoryPath') is not None:
            self.category_path = m.get('categoryPath')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ListFlowControlTaskItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: List[ListFlowControlTaskItemsResponseBodyResultDetail] = None,
        total_count: str = None,
        valid_count: str = None,
    ):
        self.detail = detail
        self.total_count = total_count
        self.valid_count = valid_count

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.valid_count is not None:
            result['validCount'] = self.valid_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListFlowControlTaskItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('validCount') is not None:
            self.valid_count = m.get('validCount')
        return self


class ListFlowControlTaskItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListFlowControlTaskItemsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListFlowControlTaskItemsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListFlowControlTaskItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowControlTaskItemsResponseBody = None,
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
            temp_model = ListFlowControlTaskItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowControlTaskReferenceResponseBodyResult(TeaModel):
    def __init__(
        self,
        last_7pv_percent: float = None,
        last_7scene_pv: float = None,
        last_7task_pv: float = None,
        last_pv_percent: float = None,
        last_scene_pv: int = None,
        last_task_pv: int = None,
        reference_id: str = None,
    ):
        # The average exposure rate of the item pool in the last seven days.
        self.last_7pv_percent = last_7pv_percent
        # The average number of exposures for the items in the selected scene in the last seven days.
        self.last_7scene_pv = last_7scene_pv
        # The average number of exposures for the item pool in the selected scene in the last seven days.
        self.last_7task_pv = last_7task_pv
        # The exposure rate of the item pool yesterday.
        self.last_pv_percent = last_pv_percent
        # The total number of exposures for the items in the selected scene yesterday.
        self.last_scene_pv = last_scene_pv
        # The number of exposures for the item pool in the selected scene yesterday.
        self.last_task_pv = last_task_pv
        # The ID of the reference data.
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_7pv_percent is not None:
            result['last7PvPercent'] = self.last_7pv_percent
        if self.last_7scene_pv is not None:
            result['last7ScenePv'] = self.last_7scene_pv
        if self.last_7task_pv is not None:
            result['last7TaskPv'] = self.last_7task_pv
        if self.last_pv_percent is not None:
            result['lastPvPercent'] = self.last_pv_percent
        if self.last_scene_pv is not None:
            result['lastScenePv'] = self.last_scene_pv
        if self.last_task_pv is not None:
            result['lastTaskPv'] = self.last_task_pv
        if self.reference_id is not None:
            result['referenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('last7PvPercent') is not None:
            self.last_7pv_percent = m.get('last7PvPercent')
        if m.get('last7ScenePv') is not None:
            self.last_7scene_pv = m.get('last7ScenePv')
        if m.get('last7TaskPv') is not None:
            self.last_7task_pv = m.get('last7TaskPv')
        if m.get('lastPvPercent') is not None:
            self.last_pv_percent = m.get('lastPvPercent')
        if m.get('lastScenePv') is not None:
            self.last_scene_pv = m.get('lastScenePv')
        if m.get('lastTaskPv') is not None:
            self.last_task_pv = m.get('lastTaskPv')
        if m.get('referenceId') is not None:
            self.reference_id = m.get('referenceId')
        return self


class ListFlowControlTaskReferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListFlowControlTaskReferenceResponseBodyResult = None,
    ):
        # The ID of the request. The value is unique for each request. This helps troubleshoot issues later.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListFlowControlTaskReferenceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListFlowControlTaskReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowControlTaskReferenceResponseBody = None,
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
            temp_model = ListFlowControlTaskReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowControlTaskReportsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListFlowControlTaskReportsResponseBodyResultMetricsDetails(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        val: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.val is not None:
            result['val'] = self.val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('val') is not None:
            self.val = m.get('val')
        return self


class ListFlowControlTaskReportsResponseBodyResultMetrics(TeaModel):
    def __init__(
        self,
        details: List[ListFlowControlTaskReportsResponseBodyResultMetricsDetails] = None,
        type: str = None,
    ):
        self.details = details
        self.type = type

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['details'] = []
        if self.details is not None:
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('details') is not None:
            for k in m.get('details'):
                temp_model = ListFlowControlTaskReportsResponseBodyResultMetricsDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListFlowControlTaskReportsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        invalid_percent: float = None,
        acc_task_ctr: float = None,
        acc_task_pv: int = None,
        acc_total_ctr: float = None,
    ):
        self.invalid_percent = invalid_percent
        self.acc_task_ctr = acc_task_ctr
        self.acc_task_pv = acc_task_pv
        self.acc_total_ctr = acc_total_ctr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_percent is not None:
            result['InvalidPercent'] = self.invalid_percent
        if self.acc_task_ctr is not None:
            result['accTaskCtr'] = self.acc_task_ctr
        if self.acc_task_pv is not None:
            result['accTaskPv'] = self.acc_task_pv
        if self.acc_total_ctr is not None:
            result['accTotalCtr'] = self.acc_total_ctr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidPercent') is not None:
            self.invalid_percent = m.get('InvalidPercent')
        if m.get('accTaskCtr') is not None:
            self.acc_task_ctr = m.get('accTaskCtr')
        if m.get('accTaskPv') is not None:
            self.acc_task_pv = m.get('accTaskPv')
        if m.get('accTotalCtr') is not None:
            self.acc_total_ctr = m.get('accTotalCtr')
        return self


class ListFlowControlTaskReportsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metrics: List[ListFlowControlTaskReportsResponseBodyResultMetrics] = None,
        total: ListFlowControlTaskReportsResponseBodyResultTotal = None,
    ):
        self.metrics = metrics
        self.total = total

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.total:
            self.total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = ListFlowControlTaskReportsResponseBodyResultMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('total') is not None:
            temp_model = ListFlowControlTaskReportsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['total'])
        return self


class ListFlowControlTaskReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListFlowControlTaskReportsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListFlowControlTaskReportsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListFlowControlTaskReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowControlTaskReportsResponseBody = None,
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
            temp_model = ListFlowControlTaskReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexVersionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        built_time: str = None,
        code: str = None,
        cost_seconds: int = None,
        flow_type: str = None,
        message: str = None,
        progress: int = None,
        rollback_enabled: bool = None,
        size: int = None,
        status: str = None,
        switched_time: str = None,
        version_id: str = None,
    ):
        self.built_time = built_time
        self.code = code
        self.cost_seconds = cost_seconds
        self.flow_type = flow_type
        self.message = message
        self.progress = progress
        self.rollback_enabled = rollback_enabled
        self.size = size
        self.status = status
        self.switched_time = switched_time
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.built_time is not None:
            result['builtTime'] = self.built_time
        if self.code is not None:
            result['code'] = self.code
        if self.cost_seconds is not None:
            result['costSeconds'] = self.cost_seconds
        if self.flow_type is not None:
            result['flowType'] = self.flow_type
        if self.message is not None:
            result['message'] = self.message
        if self.progress is not None:
            result['progress'] = self.progress
        if self.rollback_enabled is not None:
            result['rollbackEnabled'] = self.rollback_enabled
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('builtTime') is not None:
            self.built_time = m.get('builtTime')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('costSeconds') is not None:
            self.cost_seconds = m.get('costSeconds')
        if m.get('flowType') is not None:
            self.flow_type = m.get('flowType')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('rollbackEnabled') is not None:
            self.rollback_enabled = m.get('rollbackEnabled')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListIndexVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListIndexVersionsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListIndexVersionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListIndexVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndexVersionsResponseBody = None,
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
            temp_model = ListIndexVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        instance_id: str = None,
        name: str = None,
        page: int = None,
        size: int = None,
        status: str = None,
    ):
        # The state of the instance. Valid values: Running, Ready, Initializing, and Starting.
        self.expired_time = expired_time
        # The name of the instance. Fuzzy match is supported.
        self.instance_id = instance_id
        # The number of the page to return. Default value: 1.
        self.name = name
        # GET /openapi/instances?name=test&instanceId=abc&page=1&size=10
        self.page = page
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        data_set_version: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        industry: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.data_set_version = data_set_version
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.industry = industry
        self.instance_id = instance_id
        self.lock_mode = lock_mode
        self.name = name
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.data_set_version is not None:
            result['dataSetVersion'] = self.data_set_version
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.industry is not None:
            result['industry'] = self.industry
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.name is not None:
            result['name'] = self.name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('dataSetVersion') is not None:
            self.data_set_version = m.get('dataSetVersion')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListInstanceResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceTaskResponseBodyResultSubProgressInfos(TeaModel):
    def __init__(
        self,
        detail: str = None,
        finished_num: int = None,
        progress: int = None,
        total_num: int = None,
        type: str = None,
    ):
        # The detailed description of subtasks.
        self.detail = detail
        # The number of completed subtasks.
        self.finished_num = finished_num
        # The progress of subtasks.
        self.progress = progress
        # The total number of subtasks.
        self.total_num = total_num
        # The type of subtasks.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.finished_num is not None:
            result['finishedNum'] = self.finished_num
        if self.progress is not None:
            result['progress'] = self.progress
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('finishedNum') is not None:
            self.finished_num = m.get('finishedNum')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListInstanceTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        sub_progress_infos: List[ListInstanceTaskResponseBodyResultSubProgressInfos] = None,
        total_progress: int = None,
    ):
        # The name of the step. Example: DATA_IMPORT. The value indicates that data is being imported.
        self.name = name
        # The information about the progress of subtasks.
        self.sub_progress_infos = sub_progress_infos
        # The overall progress of the current task.
        self.total_progress = total_progress

    def validate(self):
        if self.sub_progress_infos:
            for k in self.sub_progress_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        result['subProgressInfos'] = []
        if self.sub_progress_infos is not None:
            for k in self.sub_progress_infos:
                result['subProgressInfos'].append(k.to_map() if k else None)
        if self.total_progress is not None:
            result['totalProgress'] = self.total_progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        self.sub_progress_infos = []
        if m.get('subProgressInfos') is not None:
            for k in m.get('subProgressInfos'):
                temp_model = ListInstanceTaskResponseBodyResultSubProgressInfos()
                self.sub_progress_infos.append(temp_model.from_map(k))
        if m.get('totalProgress') is not None:
            self.total_progress = m.get('totalProgress')
        return self


class ListInstanceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListInstanceTaskResponseBodyResult] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The progress of the task that is running on the instance.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstanceTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceTaskResponseBody = None,
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
            temp_model = ListInstanceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListItemsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        strategy_used: bool = None,
        with_invalid_detail: bool = None,
    ):
        self.page = page
        self.size = size
        self.strategy_used = strategy_used
        self.with_invalid_detail = with_invalid_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.strategy_used is not None:
            result['strategyUsed'] = self.strategy_used
        if self.with_invalid_detail is not None:
            result['withInvalidDetail'] = self.with_invalid_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('strategyUsed') is not None:
            self.strategy_used = m.get('strategyUsed')
        if m.get('withInvalidDetail') is not None:
            self.with_invalid_detail = m.get('withInvalidDetail')
        return self


class ListItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        author: str = None,
        brand_id: str = None,
        category_path: str = None,
        channel: str = None,
        duration: str = None,
        expire_time: str = None,
        item_id: str = None,
        item_type: str = None,
        pub_time: str = None,
        shop_id: str = None,
        status: str = None,
        title: str = None,
    ):
        self.author = author
        self.brand_id = brand_id
        self.category_path = category_path
        self.channel = channel
        self.duration = duration
        self.expire_time = expire_time
        self.item_id = item_id
        self.item_type = item_type
        self.pub_time = pub_time
        self.shop_id = shop_id
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['author'] = self.author
        if self.brand_id is not None:
            result['brandId'] = self.brand_id
        if self.category_path is not None:
            result['categoryPath'] = self.category_path
        if self.channel is not None:
            result['channel'] = self.channel
        if self.duration is not None:
            result['duration'] = self.duration
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.status is not None:
            result['status'] = self.status
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('brandId') is not None:
            self.brand_id = m.get('brandId')
        if m.get('categoryPath') is not None:
            self.category_path = m.get('categoryPath')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListItemsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        instance_recommend_item: int = None,
        query_count: int = None,
        scene_recommend_item: int = None,
        scene_weight_item: int = None,
        total_count: int = None,
        weight_item: int = None,
    ):
        self.instance_recommend_item = instance_recommend_item
        self.query_count = query_count
        self.scene_recommend_item = scene_recommend_item
        self.scene_weight_item = scene_weight_item
        self.total_count = total_count
        self.weight_item = weight_item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_recommend_item is not None:
            result['instanceRecommendItem'] = self.instance_recommend_item
        if self.query_count is not None:
            result['queryCount'] = self.query_count
        if self.scene_recommend_item is not None:
            result['sceneRecommendItem'] = self.scene_recommend_item
        if self.scene_weight_item is not None:
            result['sceneWeightItem'] = self.scene_weight_item
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.weight_item is not None:
            result['weightItem'] = self.weight_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceRecommendItem') is not None:
            self.instance_recommend_item = m.get('instanceRecommendItem')
        if m.get('queryCount') is not None:
            self.query_count = m.get('queryCount')
        if m.get('sceneRecommendItem') is not None:
            self.scene_recommend_item = m.get('sceneRecommendItem')
        if m.get('sceneWeightItem') is not None:
            self.scene_weight_item = m.get('sceneWeightItem')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('weightItem') is not None:
            self.weight_item = m.get('weightItem')
        return self


class ListItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: List[ListItemsResponseBodyResultDetail] = None,
        total: ListItemsResponseBodyResultTotal = None,
    ):
        self.detail = detail
        self.total = total

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()
        if self.total:
            self.total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('total') is not None:
            temp_model = ListItemsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['total'])
        return self


class ListItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListItemsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListItemsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListItemsResponseBody = None,
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
            temp_model = ListItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        page: int = None,
        query_params: str = None,
        size: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.page = page
        self.query_params = query_params
        self.size = size
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.query_params is not None:
            result['queryParams'] = self.query_params
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('queryParams') is not None:
            self.query_params = m.get('queryParams')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListLogsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListLogsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        headers: ListLogsResponseBodyHeaders = None,
        message: str = None,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        self.code = code
        self.headers = headers
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.headers is not None:
            result['headers'] = self.headers.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('headers') is not None:
            temp_model = ListLogsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['headers'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogsResponseBody = None,
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
            temp_model = ListLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMixCategoriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        categories: List[int] = None,
    ):
        # The content type.
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')
        return self


class ListMixCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListMixCategoriesResponseBodyResult] = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListMixCategoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListMixCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMixCategoriesResponseBody = None,
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
            temp_model = ListMixCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfflineStoragesResponseBodyResult(TeaModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        table_name: bytes = None,
    ):
        self.meta = meta
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['meta'] = self.meta
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class ListOfflineStoragesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: bytes = None,
        result: List[ListOfflineStoragesResponseBodyResult] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListOfflineStoragesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListOfflineStoragesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOfflineStoragesResponseBody = None,
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
            temp_model = ListOfflineStoragesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRankingModelTemplatesRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        # The number of the page to return.
        self.page = page
        # The number of entries to return on each page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListRankingModelTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[RankingModelTemplate] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = RankingModelTemplate()
                self.result.append(temp_model.from_map(k))
        return self


class ListRankingModelTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRankingModelTemplatesResponseBody = None,
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
            temp_model = ListRankingModelTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRankingModelVersionsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        status: str = None,
        template_id: str = None,
    ):
        # The number of the page to return.
        self.page = page
        # The number of entries to return on each page.
        self.size = size
        # The state of the version. Valid values: DRAFT: The version is in the draft state. EFFECTIVE: The version is effective. PUBLISHING: The version is being published. INEFFECTIVE: The version has expired. FAILED: The version has not taken effect.
        self.status = status
        # The ranking model ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class ListRankingModelVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[RankingModelVersion] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = RankingModelVersion()
                self.result.append(temp_model.from_map(k))
        return self


class ListRankingModelVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRankingModelVersionsResponseBody = None,
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
            temp_model = ListRankingModelVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRankingModelsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        ranking_model_id: str = None,
        size: int = None,
    ):
        self.page = page
        self.ranking_model_id = ranking_model_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListRankingModelsResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: Dict[str, Any] = None,
        ranking_model_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.ranking_model_id = ranking_model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        return self


class ListRankingModelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListRankingModelsResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRankingModelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRankingModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRankingModelsResponseBody = None,
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
            temp_model = ListRankingModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRankingSystemHistoriesRequest(TeaModel):
    def __init__(
        self,
        operate_type: str = None,
        page: int = None,
        size: int = None,
    ):
        # The number of the page to return.
        self.operate_type = operate_type
        # The number of entries to return on each page.
        self.page = page
        # The schema of the response parameters.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListRankingSystemHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[RankingSystemHistory] = None,
    ):
        # The returned result.
        self.request_id = request_id
        # The response body.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = RankingSystemHistory()
                self.result.append(temp_model.from_map(k))
        return self


class ListRankingSystemHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRankingSystemHistoriesResponseBody = None,
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
            temp_model = ListRankingSystemHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRankingSystemsRequest(TeaModel):
    def __init__(
        self,
        deploy_status: str = None,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        # The name of the ranking service.
        self.deploy_status = deploy_status
        # The ID of the instance.
        self.name = name
        # The state of the deployment. Valid values: NOT_DEPLOYED: The ranking service is not deployed. DEPLOY_SUCCESS: The ranking service is deployed.
        self.page = page
        # The number of the page to return.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListRankingSystemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[RankingSystem] = None,
    ):
        # The schema of the response parameters.
        self.request_id = request_id
        # The ID of the request.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = RankingSystem()
                self.result.append(temp_model.from_map(k))
        return self


class ListRankingSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRankingSystemsResponseBody = None,
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
            temp_model = ListRankingSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleConditionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        select_type: str = None,
        select_value: str = None,
        selection_operation: str = None,
    ):
        # The type of the filtering condition for the item selection rule.
        self.select_type = select_type
        # The specific value of the filtering condition for the item selection rule.
        self.select_value = select_value
        # The operation on the filtering condition for the item selection rule.
        self.selection_operation = selection_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_type is not None:
            result['selectType'] = self.select_type
        if self.select_value is not None:
            result['selectValue'] = self.select_value
        if self.selection_operation is not None:
            result['selectionOperation'] = self.selection_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        if m.get('selectValue') is not None:
            self.select_value = m.get('selectValue')
        if m.get('selectionOperation') is not None:
            self.selection_operation = m.get('selectionOperation')
        return self


class ListRuleConditionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListRuleConditionsResponseBodyResult] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRuleConditionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRuleConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRuleConditionsResponseBody = None,
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
            temp_model = ListRuleConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleTasksRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The completion rate of the task.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class ListRuleTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        finish_rate: int = None,
        finish_time: int = None,
    ):
        # The ID of the instance.
        self.finish_rate = finish_rate
        # The ID of the request.
        self.finish_time = finish_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_rate is not None:
            result['finishRate'] = self.finish_rate
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishRate') is not None:
            self.finish_rate = m.get('finishRate')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class ListRuleTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ListRuleTasksResponseBodyResult = None,
    ):
        # Queries the status of a rule-specific task.
        self.code = code
        # The ID of the scene.
        self.message = message
        # The ID of the instance.
        self.request_id = request_id
        # The error message.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListRuleTasksResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListRuleTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRuleTasksResponseBody = None,
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
            temp_model = ListRuleTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        page: int = None,
        rule_type: str = None,
        scene_id: str = None,
        size: int = None,
        start_time: int = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.page = page
        # This parameter is required.
        self.rule_type = rule_type
        # This parameter is required.
        self.scene_id = scene_id
        self.size = size
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListRulesResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.rule_id = rule_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListRulesResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRulesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesResponseBody = None,
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
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSampleFormatConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListSampleFormatConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSampleFormatConfigsResponseBody = None,
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
            temp_model = ListSampleFormatConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSamplesRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        sample_id: str = None,
        size: int = None,
    ):
        self.page = page
        self.sample_id = sample_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.sample_id is not None:
            result['sampleId'] = self.sample_id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('sampleId') is not None:
            self.sample_id = m.get('sampleId')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListSamplesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Sample] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = Sample()
                self.result.append(temp_model.from_map(k))
        return self


class ListSamplesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSamplesResponseBody = None,
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
            temp_model = ListSamplesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneItemsRequest(TeaModel):
    def __init__(
        self,
        operation_rule_id: str = None,
        page: int = None,
        preview_type: str = None,
        query_count: int = None,
        selection_rule_id: str = None,
        size: int = None,
    ):
        self.operation_rule_id = operation_rule_id
        self.page = page
        self.preview_type = preview_type
        self.query_count = query_count
        self.selection_rule_id = selection_rule_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_rule_id is not None:
            result['operationRuleId'] = self.operation_rule_id
        if self.page is not None:
            result['page'] = self.page
        if self.preview_type is not None:
            result['previewType'] = self.preview_type
        if self.query_count is not None:
            result['queryCount'] = self.query_count
        if self.selection_rule_id is not None:
            result['selectionRuleId'] = self.selection_rule_id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationRuleId') is not None:
            self.operation_rule_id = m.get('operationRuleId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')
        if m.get('queryCount') is not None:
            self.query_count = m.get('queryCount')
        if m.get('selectionRuleId') is not None:
            self.selection_rule_id = m.get('selectionRuleId')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListSceneItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        author: str = None,
        brand_id: str = None,
        category_path: str = None,
        channel: str = None,
        duration: str = None,
        expire_time: str = None,
        item_id: str = None,
        item_type: str = None,
        pub_time: str = None,
        shop_id: str = None,
        status: str = None,
        title: str = None,
    ):
        self.author = author
        self.brand_id = brand_id
        self.category_path = category_path
        self.channel = channel
        self.duration = duration
        self.expire_time = expire_time
        self.item_id = item_id
        self.item_type = item_type
        self.pub_time = pub_time
        self.shop_id = shop_id
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['author'] = self.author
        if self.brand_id is not None:
            result['brandId'] = self.brand_id
        if self.category_path is not None:
            result['categoryPath'] = self.category_path
        if self.channel is not None:
            result['channel'] = self.channel
        if self.duration is not None:
            result['duration'] = self.duration
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.status is not None:
            result['status'] = self.status
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('brandId') is not None:
            self.brand_id = m.get('brandId')
        if m.get('categoryPath') is not None:
            self.category_path = m.get('categoryPath')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListSceneItemsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        instance_recommend_item: int = None,
        scene_recommend_item: int = None,
        scene_weight_item: int = None,
        total_count: int = None,
        weight_item: int = None,
    ):
        self.instance_recommend_item = instance_recommend_item
        self.scene_recommend_item = scene_recommend_item
        self.scene_weight_item = scene_weight_item
        self.total_count = total_count
        self.weight_item = weight_item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_recommend_item is not None:
            result['instanceRecommendItem'] = self.instance_recommend_item
        if self.scene_recommend_item is not None:
            result['sceneRecommendItem'] = self.scene_recommend_item
        if self.scene_weight_item is not None:
            result['sceneWeightItem'] = self.scene_weight_item
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.weight_item is not None:
            result['weightItem'] = self.weight_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceRecommendItem') is not None:
            self.instance_recommend_item = m.get('instanceRecommendItem')
        if m.get('sceneRecommendItem') is not None:
            self.scene_recommend_item = m.get('sceneRecommendItem')
        if m.get('sceneWeightItem') is not None:
            self.scene_weight_item = m.get('sceneWeightItem')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('weightItem') is not None:
            self.weight_item = m.get('weightItem')
        return self


class ListSceneItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: List[ListSceneItemsResponseBodyResultDetail] = None,
        total: ListSceneItemsResponseBodyResultTotal = None,
    ):
        self.detail = detail
        self.total = total

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()
        if self.total:
            self.total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListSceneItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('total') is not None:
            temp_model = ListSceneItemsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['total'])
        return self


class ListSceneItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ListSceneItemsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListSceneItemsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListSceneItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSceneItemsResponseBody = None,
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
            temp_model = ListSceneItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneParametersResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: List[str] = None,
        trace_id: List[str] = None,
    ):
        self.scene_id = scene_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ListSceneParametersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ListSceneParametersResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListSceneParametersResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListSceneParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSceneParametersResponseBody = None,
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
            temp_model = ListSceneParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        scene_id: str = None,
        size: int = None,
        status: str = None,
    ):
        # Specifies whether the item can be recommended.
        self.page = page
        # The ID of the instance.
        self.scene_id = scene_id
        # The ID of the scene.
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListScenesResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListScenesResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListScenesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScenesResponseBody = None,
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
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUmengAppkeysResponseBodyResult(TeaModel):
    def __init__(
        self,
        appkey: str = None,
        name: str = None,
        platform: str = None,
    ):
        self.appkey = appkey
        self.name = name
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appkey is not None:
            result['appkey'] = self.appkey
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appkey') is not None:
            self.appkey = m.get('appkey')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class ListUmengAppkeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[ListUmengAppkeysResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUmengAppkeysResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListUmengAppkeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUmengAppkeysResponseBody = None,
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
            temp_model = ListUmengAppkeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserClustersResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListUserClustersResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        description: str = None,
        meta_type: str = None,
    ):
        self.description = description
        self.meta_type = meta_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        return self


class ListUserClustersResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ListUserClustersResponseBodyResultMeta = None,
        name: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        # meta
        self.meta = meta
        self.name = name
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ListUserClustersResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListUserClustersResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListUserClustersResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListUserClustersResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            temp_model = ListUserClustersResponseBodyHeaders()
            self.headers = temp_model.from_map(m['headers'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUserClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListUserClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserClustersResponseBody = None,
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
            temp_model = ListUserClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket_name: str = None,
        partition: str = None,
        path: str = None,
        project_name: str = None,
        table_name: str = None,
        timestamp: int = None,
        type: str = None,
    ):
        # The AccessKey ID of the Alibaba Cloud account.
        self.access_key_id = access_key_id
        # The name of the Object Storage Service (OSS) bucket.
        self.bucket_name = bucket_name
        # The partition in the MaxCompute table.
        self.partition = partition
        # The path of the OSS data source.
        self.path = path
        # The name of the MaxCompute project.
        self.project_name = project_name
        # The name of the MaxCompute table.
        self.table_name = table_name
        # The timestamp. The value must be accurate to the millisecond.
        self.timestamp = timestamp
        # The type of the data source. Only MaxCompute is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ModifyDataSourceResponseBodyResultMeta = None,
        table_name: str = None,
    ):
        # The time when the data source was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the data source was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The parameters of the data source.
        self.meta = meta
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ModifyDataSourceResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ModifyDataSourceResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details about the data source.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyDataSourceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDataSourceResponseBody = None,
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
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFeatureTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: FeatureTable = None,
    ):
        # Modifies a feature table.
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = FeatureTable()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyFeatureTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFeatureTableResponseBody = None,
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
            temp_model = ModifyFeatureTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        item_separator: str = None,
        kv_separator: str = None,
    ):
        self.item_separator = item_separator
        self.kv_separator = kv_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        index_loss_threshold: int = None,
        index_size_threshold: int = None,
        source_data_record_threshold: int = None,
        source_data_size_threshold: int = None,
    ):
        self.index_loss_threshold = index_loss_threshold
        self.index_size_threshold = index_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.source_data_size_threshold = source_data_size_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        category: str = None,
        cluster_id: str = None,
        cron: str = None,
        cron_enabled: bool = None,
        description: str = None,
        ext_info: ModifyFilteringAlgorithmMetaResponseBodyResultMetaExtInfo = None,
        meta_type: str = None,
        project_name: str = None,
        table_name: str = None,
        task_id: str = None,
        threshold: ModifyFilteringAlgorithmMetaResponseBodyResultMetaThreshold = None,
        type: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.category = category
        self.cluster_id = cluster_id
        self.cron = cron
        self.cron_enabled = cron_enabled
        self.description = description
        self.ext_info = ext_info
        self.meta_type = meta_type
        self.project_name = project_name
        self.table_name = table_name
        self.task_id = task_id
        self.threshold = threshold
        self.type = type

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.category is not None:
            result['category'] = self.category
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extInfo') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('threshold') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ModifyFilteringAlgorithmMetaResponseBodyResultMeta = None,
        status: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ModifyFilteringAlgorithmMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyFilteringAlgorithmMetaResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyFilteringAlgorithmMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFilteringAlgorithmMetaResponseBody = None,
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
            temp_model = ModifyFilteringAlgorithmMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowControlTaskRequestSelectionParams(TeaModel):
    def __init__(
        self,
        select_type: str = None,
        select_value: str = None,
        selection_operation: str = None,
    ):
        # The type of the filtering condition for the item selection rule.
        self.select_type = select_type
        # The number of filtering conditions for the item selection rule.
        self.select_value = select_value
        # The operation on the filtering condition for the item selection rule.
        self.selection_operation = selection_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_type is not None:
            result['selectType'] = self.select_type
        if self.select_value is not None:
            result['selectValue'] = self.select_value
        if self.selection_operation is not None:
            result['selectionOperation'] = self.selection_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        if m.get('selectValue') is not None:
            self.select_value = m.get('selectValue')
        if m.get('selectionOperation') is not None:
            self.selection_operation = m.get('selectionOperation')
        return self


class ModifyFlowControlTaskRequestTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        # The type of the exposure.
        self.type = type
        # The number of exposures.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ModifyFlowControlTaskRequest(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        description: str = None,
        end_time: int = None,
        meta_type: str = None,
        scene_ids: str = None,
        selection_params: List[ModifyFlowControlTaskRequestSelectionParams] = None,
        start_time: int = None,
        target: ModifyFlowControlTaskRequestTarget = None,
    ):
        # The name of the task.
        self.task_name = task_name
        # The description of the task.
        self.description = description
        # The end time. The value is a timestamp in seconds.
        self.end_time = end_time
        # The type of the metadata.
        self.meta_type = meta_type
        # The ID of the scene.
        self.scene_ids = scene_ids
        # The parameters specified for the item selection rule.
        self.selection_params = selection_params
        # The start time. The value is a timestamp in seconds.
        self.start_time = start_time
        # The settings for item exposure.
        self.target = target

    def validate(self):
        if self.selection_params:
            for k in self.selection_params:
                if k:
                    k.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        result['selectionParams'] = []
        if self.selection_params is not None:
            for k in self.selection_params:
                result['selectionParams'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        self.selection_params = []
        if m.get('selectionParams') is not None:
            for k in m.get('selectionParams'):
                temp_model = ModifyFlowControlTaskRequestSelectionParams()
                self.selection_params.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            temp_model = ModifyFlowControlTaskRequestTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class ModifyFlowControlTaskResponseBodyResultMetaSelectionParams(TeaModel):
    def __init__(
        self,
        select_type: str = None,
        select_value: str = None,
        selection_operation: str = None,
    ):
        # The type of the filtering condition for the item selection rule.
        self.select_type = select_type
        # The number of filtering conditions for the item selection rule.
        self.select_value = select_value
        # The operation on the filtering condition for the item selection rule.
        self.selection_operation = selection_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_type is not None:
            result['selectType'] = self.select_type
        if self.select_value is not None:
            result['selectValue'] = self.select_value
        if self.selection_operation is not None:
            result['selectionOperation'] = self.selection_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        if m.get('selectValue') is not None:
            self.select_value = m.get('selectValue')
        if m.get('selectionOperation') is not None:
            self.selection_operation = m.get('selectionOperation')
        return self


class ModifyFlowControlTaskResponseBodyResultMetaTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        # The type of the exposure.
        self.type = type
        # The number of exposures.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ModifyFlowControlTaskResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        description: str = None,
        end_time: int = None,
        meta_type: str = None,
        scene_ids: str = None,
        selection_params: List[ModifyFlowControlTaskResponseBodyResultMetaSelectionParams] = None,
        start_time: int = None,
        target: ModifyFlowControlTaskResponseBodyResultMetaTarget = None,
        task_name: str = None,
    ):
        # The description of the task.
        self.description = description
        # The end time. The value is a timestamp in seconds.
        self.end_time = end_time
        # The type of the metadata.
        self.meta_type = meta_type
        # The IDs of scenes.
        self.scene_ids = scene_ids
        # The parameters specified for the item selection rule.
        self.selection_params = selection_params
        # The start time. The value is a timestamp in seconds.
        self.start_time = start_time
        # The settings for item exposure.
        self.target = target
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        if self.selection_params:
            for k in self.selection_params:
                if k:
                    k.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        result['selectionParams'] = []
        if self.selection_params is not None:
            for k in self.selection_params:
                result['selectionParams'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        self.selection_params = []
        if m.get('selectionParams') is not None:
            for k in m.get('selectionParams'):
                temp_model = ModifyFlowControlTaskResponseBodyResultMetaSelectionParams()
                self.selection_params.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            temp_model = ModifyFlowControlTaskResponseBodyResultMetaTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class ModifyFlowControlTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: ModifyFlowControlTaskResponseBodyResultMeta = None,
        status: str = None,
    ):
        # The ID of the task.
        self.task_id = task_id
        # The time when the task was created.
        self.gmt_create = gmt_create
        # The time when the task was modified.
        self.gmt_modified = gmt_modified
        # The metadata.
        self.meta = meta
        # The state of the task.
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = ModifyFlowControlTaskResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ModifyFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyFlowControlTaskResponseBodyResult = None,
    ):
        # The ID of the request. The value is unique for each request. This facilitates troubleshooting.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyFlowControlTaskResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowControlTaskResponseBody = None,
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
            temp_model = ModifyFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        data_set_version: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        industry: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The billing method. Valid values: PrePaid and PostPaid. Only the PrePaid billing method is supported.
        self.charge_type = charge_type
        # The commodity code of the recommended item.
        self.commodity_code = commodity_code
        # The version of the dataset that provides online services.
        self.data_set_version = data_set_version
        # The time when the instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format.The time is displayed in UTC.
        self.expired_time = expired_time
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the instance was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The type of the industry. Valid values: content, item, news, video, and sns.
        self.industry = industry
        # The instance ID.
        self.instance_id = instance_id
        # The lock mode of the instance. Valid values: Unlock, ManualLock, and LockByExpiration.
        self.lock_mode = lock_mode
        # The name of the instance.
        self.name = name
        # The region where the instance resides.
        self.region_id = region_id
        # The state of the instance. Valid values: Initializing, Ready, and Running.
        self.status = status
        # The type of the instance. Only the Standard edition is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.data_set_version is not None:
            result['dataSetVersion'] = self.data_set_version
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.industry is not None:
            result['industry'] = self.industry
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.name is not None:
            result['name'] = self.name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('dataSetVersion') is not None:
            self.data_set_version = m.get('dataSetVersion')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ModifyInstanceResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceResponseBody = None,
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
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyItemsResponseBody = None,
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
            temp_model = ModifyItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfflineStoragesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: bytes = None,
        result: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyOfflineStoragesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOfflineStoragesResponseBody = None,
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
            temp_model = ModifyOfflineStoragesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: Dict[str, Any] = None,
        ranking_model_id: str = None,
    ):
        # The error message.
        self.gmt_create = gmt_create
        # The ID of the request.
        self.gmt_modified = gmt_modified
        # __null__
        self.meta = meta
        # The error code.
        self.ranking_model_id = ranking_model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        return self


class ModifyRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ModifyRankingModelResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        # The data source of the filtering table. Only MaxCompute tables are supported.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRankingModelResponseBody = None,
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
            temp_model = ModifyRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRankingModelTemplateRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyRankingModelTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingModelTemplate = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the ranking model.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingModelTemplate()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyRankingModelTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRankingModelTemplateResponseBody = None,
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
            temp_model = ModifyRankingModelTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRankingSystemRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The configurations that you want to modify.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RankingSystem = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ranking service that was modified.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RankingSystem()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRankingSystemResponseBody = None,
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
            temp_model = ModifyRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
        rule_meta: Dict[str, Any] = None,
        status: str = None,
    ):
        # The time when the rule was created.
        self.gmt_create = gmt_create
        # The time when the rule was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the rule.
        self.rule_id = rule_id
        # The specific information about the rule.
        self.rule_meta = rule_meta
        # Indicates whether the rule is enabled. Valid values: true and false.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_meta is not None:
            result['ruleMeta'] = self.rule_meta
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleMeta') is not None:
            self.rule_meta = m.get('ruleMeta')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ModifyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ModifyRuleResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRuleResponseBody = None,
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
            temp_model = ModifyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySampleRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifySampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Sample = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = Sample()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifySampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySampleResponseBody = None,
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
            temp_model = ModifySampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ModifySceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ModifySceneResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifySceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifySceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySceneResponseBody = None,
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
            temp_model = ModifySceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineFilteringAlgorithmResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        item_separator: str = None,
        kv_separator: str = None,
    ):
        self.item_separator = item_separator
        self.kv_separator = kv_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        return self


class OfflineFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        index_loss_threshold: int = None,
        index_size_threshold: int = None,
        source_data_record_threshold: int = None,
        source_data_size_threshold: int = None,
    ):
        self.index_loss_threshold = index_loss_threshold
        self.index_size_threshold = index_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.source_data_size_threshold = source_data_size_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        return self


class OfflineFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        category: str = None,
        cluster_id: str = None,
        cron: str = None,
        cron_enabled: bool = None,
        description: str = None,
        ext_info: OfflineFilteringAlgorithmResponseBodyResultMetaExtInfo = None,
        meta_type: str = None,
        project_name: str = None,
        table_name: str = None,
        task_id: str = None,
        threshold: OfflineFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        type: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.category = category
        self.cluster_id = cluster_id
        self.cron = cron
        self.cron_enabled = cron_enabled
        self.description = description
        self.ext_info = ext_info
        self.meta_type = meta_type
        self.project_name = project_name
        self.table_name = table_name
        self.task_id = task_id
        self.threshold = threshold
        self.type = type

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.category is not None:
            result['category'] = self.category
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extInfo') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('threshold') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OfflineFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta: OfflineFilteringAlgorithmResponseBodyResultMeta = None,
        status: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta = meta
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('meta') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class OfflineFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: OfflineFilteringAlgorithmResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class OfflineFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineFilteringAlgorithmResponseBody = None,
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
            temp_model = OfflineFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PublishFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishFlowControlTaskResponseBody = None,
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
            temp_model = PublishFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRuleRequest(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        scene_id: str = None,
    ):
        # The type of the rule. Example: selection and operation.
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The scene ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class PublishRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        # The rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class PublishRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: PublishRuleResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = PublishRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class PublishRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishRuleResponseBody = None,
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
            temp_model = PublishRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushColdStartDocumentRequestBody(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        fields: Any = None,
    ):
        self.cmd = cmd
        self.fields = fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.fields is not None:
            result['fields'] = self.fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        return self


class PushColdStartDocumentRequest(TeaModel):
    def __init__(
        self,
        body: List[PushColdStartDocumentRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = PushColdStartDocumentRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class PushColdStartDocumentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushColdStartDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushColdStartDocumentResponseBody = None,
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
            temp_model = PushColdStartDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        # true/false
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushDocumentResponseBody = None,
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
            temp_model = PushDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushInterventionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushInterventionResponseBody = None,
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
            temp_model = PushInterventionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataMessageRequest(TeaModel):
    def __init__(
        self,
        bhv_type: str = None,
        cmd_type: str = None,
        end_time: int = None,
        imei: str = None,
        item_id: str = None,
        item_type: str = None,
        message_source: str = None,
        page: int = None,
        scene_id: str = None,
        size: int = None,
        start_time: int = None,
        trace_id: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.bhv_type = bhv_type
        self.cmd_type = cmd_type
        # This parameter is required.
        self.end_time = end_time
        self.imei = imei
        self.item_id = item_id
        self.item_type = item_type
        self.message_source = message_source
        self.page = page
        self.scene_id = scene_id
        self.size = size
        # This parameter is required.
        self.start_time = start_time
        self.trace_id = trace_id
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bhv_type is not None:
            result['bhvType'] = self.bhv_type
        if self.cmd_type is not None:
            result['cmdType'] = self.cmd_type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.imei is not None:
            result['imei'] = self.imei
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.message_source is not None:
            result['messageSource'] = self.message_source
        if self.page is not None:
            result['page'] = self.page
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bhvType') is not None:
            self.bhv_type = m.get('bhvType')
        if m.get('cmdType') is not None:
            self.cmd_type = m.get('cmdType')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('messageSource') is not None:
            self.message_source = m.get('messageSource')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self


class QueryDataMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryDataMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDataMessageResponseBody = None,
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
            temp_model = QueryDataMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataMessageStatisticsRequest(TeaModel):
    def __init__(
        self,
        bhv_type: str = None,
        cmd_type: str = None,
        end_time: int = None,
        imei: str = None,
        item_id: str = None,
        item_type: str = None,
        message_source: str = None,
        scene_id: str = None,
        start_time: int = None,
        trace_id: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The type of behaviors. Valid values: expose, click, like, comment, collect, stay, cart, buy, and evaluate.
        self.bhv_type = bhv_type
        # The type of the operation. Valid values: update, delete, and add.
        self.cmd_type = cmd_type
        # The end time. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.imei = imei
        # The ID of the item. This parameter is required when the value of table is set to item.
        self.item_id = item_id
        # The type of the item. This parameter is required when the value of table is set to item.
        self.item_type = item_type
        # The source of the operation. Valid values:
        # 
        # CONSOLE and FEEDER.
        self.message_source = message_source
        # The scene ID.
        self.scene_id = scene_id
        # The start time. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The event tracking ID.
        self.trace_id = trace_id
        # The ID of the user. This parameter is required when the value of table is set to user.
        self.user_id = user_id
        # The type of the user. This parameter is required when the value of table is set to user.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bhv_type is not None:
            result['bhvType'] = self.bhv_type
        if self.cmd_type is not None:
            result['cmdType'] = self.cmd_type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.imei is not None:
            result['imei'] = self.imei
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.message_source is not None:
            result['messageSource'] = self.message_source
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bhvType') is not None:
            self.bhv_type = m.get('bhvType')
        if m.get('cmdType') is not None:
            self.cmd_type = m.get('cmdType')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('messageSource') is not None:
            self.message_source = m.get('messageSource')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self


class QueryDataMessageStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryDataMessageStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDataMessageStatisticsResponseBody = None,
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
            temp_model = QueryDataMessageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExceptionHistoryRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryExceptionHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryExceptionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExceptionHistoryResponseBody = None,
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
            temp_model = QueryExceptionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRawDataRequest(TeaModel):
    def __init__(
        self,
        imei: str = None,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.imei = imei
        # The item ID. This parameter is required when the table parameter is set to item.
        self.item_id = item_id
        # The type of the item. This parameter is required when the table parameter is set to item.
        self.item_type = item_type
        # The user ID. This parameter is required when the table parameter is set to user.
        self.user_id = user_id
        # The type of the user. This parameter is required when the table parameter is set to user.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.imei is not None:
            result['imei'] = self.imei
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self


class QueryRawDataResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The error message.
        self.message = message
        # The error code.
        self.code = code
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryRawDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRawDataResponseBody = None,
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
            temp_model = QueryRawDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleAggregationReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QuerySingleAggregationReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySingleAggregationReportResponseBody = None,
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
            temp_model = QuerySingleAggregationReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleReportRequest(TeaModel):
    def __init__(
        self,
        report_type: str = None,
    ):
        # The type of the single table report. This parameter is required.
        # 
        # Valid values: typeItemValidScene,
        # 
        # typeItemTag,
        # 
        # typeItemTagScene,
        # 
        # typeItemWeightScene,
        # 
        # typeItemRawScene, and
        # 
        # typeItemExpireScene
        # 
        # This parameter is required.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_type is not None:
            result['reportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reportType') is not None:
            self.report_type = m.get('reportType')
        return self


class QuerySingleReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QuerySingleReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySingleReportResponseBody = None,
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
            temp_model = QuerySingleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySyncReportAggregationRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end time. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class QuerySyncReportAggregationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QuerySyncReportAggregationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySyncReportAggregationResponseBody = None,
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
            temp_model = QuerySyncReportAggregationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RebuildIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebuildIndexResponseBody = None,
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
            temp_model = RebuildIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecommendRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        imei: str = None,
        ip: str = None,
        items: str = None,
        rank_open: bool = None,
        rec_type: str = None,
        return_count: int = None,
        scene_id: str = None,
        service_type: str = None,
        strategy: str = None,
        user_id: str = None,
        user_info: str = None,
    ):
        # The status of the execution.
        self.filter = filter
        # The ID of the scene in which the item is to be recommended.
        self.imei = imei
        # The HTTP status code.
        self.ip = ip
        # The information about event tracking. The value of this parameter varies based on different items and needs to be uploaded together with the corresponding behavior data.
        self.items = items
        # N/A
        self.rank_open = rank_open
        # The type of the recommended item.
        self.rec_type = rec_type
        # The returned results.
        # 
        # This parameter is required.
        self.return_count = return_count
        # The number of result entries to return. Valid values: 0 to 50.
        self.scene_id = scene_id
        # The position at which the recommended item is displayed. The position number starts from 0. The return results are ranked by position. You can ignore this parameter.
        self.service_type = service_type
        # 如果需要使用坑位策略，请求参数内新增strategy="fixedSlot"，此时系统将按照坑位配置返回推荐结果
        self.strategy = strategy
        # The items used for related recommendations in specified scenes.
        self.user_id = user_id
        # The ID of the request.
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.imei is not None:
            result['imei'] = self.imei
        if self.ip is not None:
            result['ip'] = self.ip
        if self.items is not None:
            result['items'] = self.items
        if self.rank_open is not None:
            result['rankOpen'] = self.rank_open
        if self.rec_type is not None:
            result['recType'] = self.rec_type
        if self.return_count is not None:
            result['returnCount'] = self.return_count
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.strategy is not None:
            result['strategy'] = self.strategy
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_info is not None:
            result['userInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('items') is not None:
            self.items = m.get('items')
        if m.get('rankOpen') is not None:
            self.rank_open = m.get('rankOpen')
        if m.get('recType') is not None:
            self.rec_type = m.get('recType')
        if m.get('returnCount') is not None:
            self.return_count = m.get('returnCount')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userInfo') is not None:
            self.user_info = m.get('userInfo')
        return self


class RecommendResponseBodyResult(TeaModel):
    def __init__(
        self,
        flow_weight: float = None,
        item_id: str = None,
        item_type: str = None,
        match_info: str = None,
        message: str = None,
        position: int = None,
        trace_id: str = None,
        trace_info: str = None,
        weight: float = None,
    ):
        # The ID of the device.
        self.flow_weight = flow_weight
        # The returned results.
        self.item_id = item_id
        # The ID of the recommended item.
        self.item_type = item_type
        # N/A
        self.match_info = match_info
        # The event tracking ID. This parameter is uploaded together with user behaviors on the recommended item. In this case, the value of this parameter is ali.
        self.message = message
        # The string for filtering during recommendation.
        self.position = position
        # The status of the execution.
        self.trace_id = trace_id
        # Specifies whether to perform personalized ranking based on the user IDs in the filtering and ranking phases.
        self.trace_info = trace_info
        # The weight of the recommended item.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_weight is not None:
            result['flowWeight'] = self.flow_weight
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.match_info is not None:
            result['matchInfo'] = self.match_info
        if self.message is not None:
            result['message'] = self.message
        if self.position is not None:
            result['position'] = self.position
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.trace_info is not None:
            result['traceInfo'] = self.trace_info
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowWeight') is not None:
            self.flow_weight = m.get('flowWeight')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('matchInfo') is not None:
            self.match_info = m.get('matchInfo')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('traceInfo') is not None:
            self.trace_info = m.get('traceInfo')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RecommendResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[RecommendResponseBodyResult] = None,
    ):
        # This parameter may be used in the debugging process. You can ignore this parameter.
        self.code = code
        # Queries the recommendation results of a specified instance.
        self.message = message
        # The weight of the specified process.
        self.request_id = request_id
        # The unique ID of the user.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = RecommendResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class RecommendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecommendResponseBody = None,
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
            temp_model = RecommendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshFeatureTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: FeatureTable = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = FeatureTable()
            self.result = temp_model.from_map(m['result'])
        return self


class RefreshFeatureTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshFeatureTableResponseBody = None,
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
            temp_model = RefreshFeatureTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackRankingSystemRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RollbackRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RollbackRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RollbackRankingSystemResponseBody = None,
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
            temp_model = RollbackRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether a dataset was created.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RunInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunInstanceResponseBody = None,
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
            temp_model = RunInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunRankingModelTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RunRankingModelTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunRankingModelTemplateResponseBody = None,
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
            temp_model = RunRankingModelTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunSampleFormatConfigRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
    ):
        # The mode of the formatting. Default value: Latest. This value indicates that the latest formatting configurations are used.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        return self


class RunSampleFormatConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # The instance ID.
        self.request_id = request_id
        # Indicates whether the sample formatting configurations are triggered.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RunSampleFormatConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunSampleFormatConfigResponseBody = None,
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
            temp_model = RunSampleFormatConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        state: str = None,
        version_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.state = state
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.state is not None:
            result['state'] = self.state
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class StopDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: StopDataSetResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = StopDataSetResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class StopDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDataSetResponseBody = None,
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
            temp_model = StopDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopFlowControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StopFlowControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopFlowControlTaskResponseBody = None,
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
            temp_model = StopFlowControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnLockIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UnLockIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnLockIndexVersionResponseBody = None,
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
            temp_model = UnLockIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentBasicInfoResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        # The default value of the algorithm configuration item.
        self.default_value = default_value
        # The custom value of the algorithm configuration item.
        self.experiment_value = experiment_value
        # The key of the algorithm configuration item.
        self.key = key
        # The name of the algorithm configuration item.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentBasicInfoResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[UpdateExperimentBasicInfoResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        # The category of the algorithm.
        self.category = category
        # The information about the child configuration item.
        self.config = config
        # The default value of the algorithm.
        self.default_value = default_value
        # The custom value of the algorithm.
        self.experiment_value = experiment_value
        # Indicates whether child configuration items exist. Valid values: true and false.
        self.has_config = has_config
        # The key of the algorithm.
        self.key = key
        # The name of the experiment.
        self.name = name
        # The type of the algorithm.
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = UpdateExperimentBasicInfoResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateExperimentBasicInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithms: List[UpdateExperimentBasicInfoResponseBodyResultAlgorithms] = None,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        # The parameters of the experiment.
        self.algorithms = algorithms
        # Indicates whether the experiment uses default configurations.
        self.base = base
        # The traffic buckets.
        self.buckets = buckets
        # The description of the experiment.
        self.description = description
        # The experiment ID.
        self.experiment_id = experiment_id
        # The name of the experiment.
        self.name = name
        # The time when the experiment was unpublished.
        self.offline_time = offline_time
        # The time when the experiment was published.
        self.online_time = online_time
        # The status of the experiment.
        self.status = status

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = UpdateExperimentBasicInfoResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateExperimentBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateExperimentBasicInfoResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the experiment.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateExperimentBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateExperimentBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentBasicInfoResponseBody = None,
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
            temp_model = UpdateExperimentBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentConfigResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.key = key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentConfigResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[UpdateExperimentConfigResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        self.category = category
        self.config = config
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.key = key
        self.name = name
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = UpdateExperimentConfigResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateExperimentConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithms: List[UpdateExperimentConfigResponseBodyResultAlgorithms] = None,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        self.algorithms = algorithms
        self.base = base
        self.buckets = buckets
        self.description = description
        self.experiment_id = experiment_id
        self.name = name
        self.offline_time = offline_time
        self.online_time = online_time
        self.status = status

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = UpdateExperimentConfigResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateExperimentConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateExperimentConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateExperimentConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateExperimentConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentConfigResponseBody = None,
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
            temp_model = UpdateExperimentConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentStatusResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        experiment_value: str = None,
        key: str = None,
        name: str = None,
    ):
        # The default value of the algorithm. If you set key to i2i, hot, or new, the value of this parameter is true or false. If you set key to mtorder, the value of this parameter is a list of filtering algorithms ranked by priority.
        self.default_value = default_value
        # The custom value of the algorithm.
        self.experiment_value = experiment_value
        # The algorithm key. Valid values: i2i: the I2I filtering algorithm. u2x2i: the U2X2I filtering algorithm. hot: the filtering algorithm for popular items. new: the filtering algorithm for new items. embedding: the vector filtering algorithm. mtorder: the priority of the filtering algorithm. rankservice: the ranking service.
        self.key = key
        # The algorithm name. (Note: If you use the default algorithm, the console obtains the algorithm name from Medusa. If you customize an algorithm for the experiment, the algorithm name is directly returned.)
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentStatusResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: List[UpdateExperimentStatusResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        key: str = None,
        name: str = None,
        type: str = None,
    ):
        # The algorithm category. Valid values: RECALL and RANK.
        self.category = category
        # The experiment configurations.
        self.config = config
        # The default value of the algorithm configuration item.
        self.default_value = default_value
        # The custom value of the algorithm configuration item.
        self.experiment_value = experiment_value
        # Indicates whether child configuration items exist. Valid values: true and false.
        self.has_config = has_config
        # The algorithm key. Valid values: i2i: the I2I filtering algorithm. u2x2i: the U2X2I filtering algorithm. hot: the filtering algorithm for popular items. new: the filtering algorithm for new items. embedding: the vector filtering algorithm. mtorder: the priority of the filtering algorithm. rankservice: the ranking service.
        self.key = key
        # The algorithm name. (Note: If you use the default algorithm, the console obtains the algorithm name from Medusa. If you customize an algorithm for the experiment, the algorithm name is directly returned.)
        self.name = name
        # The algorithm type. Valid values: SYSTEM and CUSTOM.
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = UpdateExperimentStatusResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateExperimentStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        algorithms: List[UpdateExperimentStatusResponseBodyResultAlgorithms] = None,
        base: bool = None,
        buckets: List[str] = None,
        description: str = None,
        experiment_id: str = None,
        name: str = None,
        offline_time: str = None,
        online_time: str = None,
        status: str = None,
    ):
        # The algorithm configurations.
        self.algorithms = algorithms
        # Indicates whether the default configurations are used for the experiment.
        self.base = base
        # The buckets. This parameter takes effect only when the experiment is published.
        self.buckets = buckets
        # The remarks of the experiment.
        self.description = description
        # The experiment ID.
        self.experiment_id = experiment_id
        # The experiment name.
        self.name = name
        # The time when the experiment was unpublished.
        self.offline_time = offline_time
        # The time when the experiment was published.
        self.online_time = online_time
        # The experiment state. Valid values: init, online, finish, and offline.
        self.status = status

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.base is not None:
            result['base'] = self.base
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.description is not None:
            result['description'] = self.description
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = UpdateExperimentStatusResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateExperimentStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateExperimentStatusResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateExperimentStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateExperimentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentStatusResponseBody = None,
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
            temp_model = UpdateExperimentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UpgradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: UpgradeInstanceResponseBodyResult = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpgradeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpgradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeInstanceResponseBody = None,
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
            temp_model = UpgradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ValidateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateInstanceResponseBody = None,
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
            temp_model = ValidateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyRankingSystemRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class VerifyRankingSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class VerifyRankingSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyRankingSystemResponseBody = None,
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
            temp_model = VerifyRankingSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


