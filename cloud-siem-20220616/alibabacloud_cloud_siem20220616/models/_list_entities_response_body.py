# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListEntitiesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.ListEntitiesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEntitiesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListEntitiesResponseBodyDataPageInfo = None,
        response_data: List[main_models.ListEntitiesResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for v1 in self.response_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ResponseData'] = []
        if self.response_data is not None:
            for k1 in self.response_data:
                result['ResponseData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListEntitiesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.ListEntitiesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class ListEntitiesResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        agent_confidence: str = None,
        agent_disposal_method: str = None,
        agent_disposal_playbook_uuid: str = None,
        agent_disposal_suggestion: str = None,
        alert_num: int = None,
        alert_uuid: str = None,
        aliuid: int = None,
        cloud_code: str = None,
        entity_id: str = None,
        entity_info: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        event_num: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        is_asset: str = None,
        is_malware: str = None,
        malware_type: str = None,
        sub_user_id: int = None,
        tags: str = None,
    ):
        self.agent_confidence = agent_confidence
        self.agent_disposal_method = agent_disposal_method
        self.agent_disposal_playbook_uuid = agent_disposal_playbook_uuid
        self.agent_disposal_suggestion = agent_disposal_suggestion
        self.alert_num = alert_num
        self.alert_uuid = alert_uuid
        self.aliuid = aliuid
        self.cloud_code = cloud_code
        self.entity_id = entity_id
        self.entity_info = entity_info
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.entity_uuid = entity_uuid
        self.event_num = event_num
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.is_asset = is_asset
        self.is_malware = is_malware
        self.malware_type = malware_type
        self.sub_user_id = sub_user_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_confidence is not None:
            result['AgentConfidence'] = self.agent_confidence

        if self.agent_disposal_method is not None:
            result['AgentDisposalMethod'] = self.agent_disposal_method

        if self.agent_disposal_playbook_uuid is not None:
            result['AgentDisposalPlaybookUuid'] = self.agent_disposal_playbook_uuid

        if self.agent_disposal_suggestion is not None:
            result['AgentDisposalSuggestion'] = self.agent_disposal_suggestion

        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num

        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.event_num is not None:
            result['EventNum'] = self.event_num

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.is_asset is not None:
            result['IsAsset'] = self.is_asset

        if self.is_malware is not None:
            result['IsMalware'] = self.is_malware

        if self.malware_type is not None:
            result['MalwareType'] = self.malware_type

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentConfidence') is not None:
            self.agent_confidence = m.get('AgentConfidence')

        if m.get('AgentDisposalMethod') is not None:
            self.agent_disposal_method = m.get('AgentDisposalMethod')

        if m.get('AgentDisposalPlaybookUuid') is not None:
            self.agent_disposal_playbook_uuid = m.get('AgentDisposalPlaybookUuid')

        if m.get('AgentDisposalSuggestion') is not None:
            self.agent_disposal_suggestion = m.get('AgentDisposalSuggestion')

        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')

        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('IsAsset') is not None:
            self.is_asset = m.get('IsAsset')

        if m.get('IsMalware') is not None:
            self.is_malware = m.get('IsMalware')

        if m.get('MalwareType') is not None:
            self.malware_type = m.get('MalwareType')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class ListEntitiesResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

