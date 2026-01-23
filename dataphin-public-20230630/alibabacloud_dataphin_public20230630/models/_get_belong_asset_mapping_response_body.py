# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBelongAssetMappingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        mapping_relation_list: List[main_models.GetBelongAssetMappingResponseBodyMappingRelationList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.mapping_relation_list = mapping_relation_list
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.mapping_relation_list:
            for v1 in self.mapping_relation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['MappingRelationList'] = []
        if self.mapping_relation_list is not None:
            for k1 in self.mapping_relation_list:
                result['MappingRelationList'].append(k1.to_map() if k1 else None)

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.mapping_relation_list = []
        if m.get('MappingRelationList') is not None:
            for k1 in m.get('MappingRelationList'):
                temp_model = main_models.GetBelongAssetMappingResponseBodyMappingRelationList()
                self.mapping_relation_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBelongAssetMappingResponseBodyMappingRelationList(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        guid: str = None,
        modify_time: str = None,
        name: str = None,
        standard_code: str = None,
        standard_id: int = None,
        standard_name: str = None,
        standard_set_directory: str = None,
        standard_set_id: int = None,
        standard_set_name: str = None,
        standard_stage: str = None,
    ):
        self.asset_type = asset_type
        self.guid = guid
        self.modify_time = modify_time
        self.name = name
        self.standard_code = standard_code
        self.standard_id = standard_id
        self.standard_name = standard_name
        self.standard_set_directory = standard_set_directory
        self.standard_set_id = standard_set_id
        self.standard_set_name = standard_set_name
        self.standard_stage = standard_stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.standard_code is not None:
            result['StandardCode'] = self.standard_code

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.standard_name is not None:
            result['StandardName'] = self.standard_name

        if self.standard_set_directory is not None:
            result['StandardSetDirectory'] = self.standard_set_directory

        if self.standard_set_id is not None:
            result['StandardSetId'] = self.standard_set_id

        if self.standard_set_name is not None:
            result['StandardSetName'] = self.standard_set_name

        if self.standard_stage is not None:
            result['StandardStage'] = self.standard_stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StandardCode') is not None:
            self.standard_code = m.get('StandardCode')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('StandardName') is not None:
            self.standard_name = m.get('StandardName')

        if m.get('StandardSetDirectory') is not None:
            self.standard_set_directory = m.get('StandardSetDirectory')

        if m.get('StandardSetId') is not None:
            self.standard_set_id = m.get('StandardSetId')

        if m.get('StandardSetName') is not None:
            self.standard_set_name = m.get('StandardSetName')

        if m.get('StandardStage') is not None:
            self.standard_stage = m.get('StandardStage')

        return self

