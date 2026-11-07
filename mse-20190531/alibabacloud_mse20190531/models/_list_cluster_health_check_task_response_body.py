# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListClusterHealthCheckTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListClusterHealthCheckTaskResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code is only used to synchronize with success
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic part in the error message.
        self.dynamic_code = dynamic_code
        # The dynamic error message used to replace \\*\\*%s\\*\\* in the **ErrMessage** parameter.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid**, and **DynamicMessage** returns **DtsJobId**, it indicates that the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code. Take note of the following items:
        # 
        # - Successful request: The **ErrorCode** field is not returned.
        # 
        # - Failed request: The **ErrorCode** field is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - `true`: The request was successful.
        # 
        # - `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListClusterHealthCheckTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListClusterHealthCheckTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListClusterHealthCheckTaskResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number of the list.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of health check tasks.
        self.result = result
        # The total number of queried rules.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListClusterHealthCheckTaskResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListClusterHealthCheckTaskResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        charge_type: str = None,
        cluster_type: str = None,
        create_time: str = None,
        id: int = None,
        image_version: str = None,
        instance_id: str = None,
        primary_user: str = None,
        replica: str = None,
        risk_list: List[main_models.ListClusterHealthCheckTaskResponseBodyDataResultRiskList] = None,
        score: int = None,
        spec: str = None,
        status: str = None,
        total_item: int = None,
        total_risk: int = None,
        type: str = None,
        update_time: str = None,
        version_code: str = None,
    ):
        # The complete version number.
        self.app_version = app_version
        # The billing method.
        self.charge_type = charge_type
        # The type of the instance.
        self.cluster_type = cluster_type
        # The time when the task was created.
        self.create_time = create_time
        # The ID.
        self.id = id
        # Redundant field.
        self.image_version = image_version
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the user to which the cluster belongs.
        self.primary_user = primary_user
        # The number of nodes in the cluster.
        self.replica = replica
        # The list of risk items.
        self.risk_list = risk_list
        # The total score.
        self.score = score
        # The specifications.
        self.spec = spec
        # The job states.
        self.status = status
        # The total number of inspection items.
        self.total_item = total_item
        # The total number of risk items.
        self.total_risk = total_risk
        # Redundant field.
        self.type = type
        # The time when the instance was last updated.
        self.update_time = update_time
        # The version number.
        self.version_code = version_code

    def validate(self):
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user

        if self.replica is not None:
            result['Replica'] = self.replica

        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['Score'] = self.score

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_risk is not None:
            result['TotalRisk'] = self.total_risk

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.ListClusterHealthCheckTaskResponseBodyDataResultRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalRisk') is not None:
            self.total_risk = m.get('TotalRisk')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class ListClusterHealthCheckTaskResponseBodyDataResultRiskList(DaraModel):
    def __init__(
        self,
        description: str = None,
        description_en: str = None,
        id: int = None,
        module: str = None,
        mute: bool = None,
        notice_feature: bool = None,
        primary_user: str = None,
        risk_code: str = None,
        risk_level: str = None,
        risk_name: str = None,
        risk_name_en: str = None,
        risk_type: str = None,
        situation: str = None,
        situation_en: str = None,
        suggestion: str = None,
        suggestion_en: str = None,
        task_id: int = None,
        type: int = None,
        values: str = None,
    ):
        # The description.
        self.description = description
        # The English description of the risk.
        self.description_en = description_en
        # The ID.
        self.id = id
        # Redundant field.
        self.module = module
        # Specifies whether to disable the notification feature if the risk item occurs.
        # 
        # - true: Disables risk item notifications
        # 
        # - false: Enables risk item notifications
        self.mute = mute
        # Redundant field.
        self.notice_feature = notice_feature
        # The ID of the user to which the cluster belongs.
        self.primary_user = primary_user
        # The risk code.
        self.risk_code = risk_code
        # The risk level. Valid values:
        # 
        # - HIGH: High risk
        # 
        # - MID: Medium risk
        # 
        # - LOW: Low risk
        self.risk_level = risk_level
        # The risk name.
        self.risk_name = risk_name
        # The English name of the risk.
        self.risk_name_en = risk_name_en
        # The type of the risk.
        self.risk_type = risk_type
        # The current situation.
        self.situation = situation
        # The English description of the current situation.
        self.situation_en = situation_en
        # The suggestion.
        self.suggestion = suggestion
        # The English description of the suggestion.
        self.suggestion_en = suggestion_en
        # The ID of the associated parent task.
        self.task_id = task_id
        # Redundant field.
        self.type = type
        # Redundant field.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en

        if self.id is not None:
            result['Id'] = self.id

        if self.module is not None:
            result['Module'] = self.module

        if self.mute is not None:
            result['Mute'] = self.mute

        if self.notice_feature is not None:
            result['NoticeFeature'] = self.notice_feature

        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user

        if self.risk_code is not None:
            result['RiskCode'] = self.risk_code

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.risk_name_en is not None:
            result['RiskNameEn'] = self.risk_name_en

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.situation is not None:
            result['Situation'] = self.situation

        if self.situation_en is not None:
            result['SituationEn'] = self.situation_en

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.suggestion_en is not None:
            result['SuggestionEn'] = self.suggestion_en

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('Mute') is not None:
            self.mute = m.get('Mute')

        if m.get('NoticeFeature') is not None:
            self.notice_feature = m.get('NoticeFeature')

        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')

        if m.get('RiskCode') is not None:
            self.risk_code = m.get('RiskCode')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('RiskNameEn') is not None:
            self.risk_name_en = m.get('RiskNameEn')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('Situation') is not None:
            self.situation = m.get('Situation')

        if m.get('SituationEn') is not None:
            self.situation_en = m.get('SituationEn')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('SuggestionEn') is not None:
            self.suggestion_en = m.get('SuggestionEn')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

