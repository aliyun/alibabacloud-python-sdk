# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAssetAttributesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAssetAttributesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.GetAssetAttributesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAssetAttributesResponseBodyData(DaraModel):
    def __init__(
        self,
        asset_attribute_list: List[main_models.GetAssetAttributesResponseBodyDataAssetAttributeList] = None,
    ):
        # The list of asset properties.
        self.asset_attribute_list = asset_attribute_list

    def validate(self):
        if self.asset_attribute_list:
            for v1 in self.asset_attribute_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetAttributeList'] = []
        if self.asset_attribute_list is not None:
            for k1 in self.asset_attribute_list:
                result['AssetAttributeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_attribute_list = []
        if m.get('AssetAttributeList') is not None:
            for k1 in m.get('AssetAttributeList'):
                temp_model = main_models.GetAssetAttributesResponseBodyDataAssetAttributeList()
                self.asset_attribute_list.append(temp_model.from_map(k1))

        return self

class GetAssetAttributesResponseBodyDataAssetAttributeList(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        asset_type: str = None,
        attribute_list: List[main_models.GetAssetAttributesResponseBodyDataAssetAttributeListAttributeList] = None,
        guid: str = None,
        last_modified_time: str = None,
    ):
        # The asset name.
        self.asset_name = asset_name
        # The asset type.
        self.asset_type = asset_type
        # The list of property values.
        self.attribute_list = attribute_list
        # The unique identifier of the asset.
        self.guid = guid
        # The last modified time, in the format of yyyy-MM-dd HH:mm:ss.
        self.last_modified_time = last_modified_time

    def validate(self):
        if self.attribute_list:
            for v1 in self.attribute_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k1 in self.attribute_list:
                result['AttributeList'].append(k1.to_map() if k1 else None)

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k1 in m.get('AttributeList'):
                temp_model = main_models.GetAssetAttributesResponseBodyDataAssetAttributeListAttributeList()
                self.attribute_list.append(temp_model.from_map(k1))

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        return self

class GetAssetAttributesResponseBodyDataAssetAttributeListAttributeList(DaraModel):
    def __init__(
        self,
        attribute_code: str = None,
        attribute_name: str = None,
        required: bool = None,
        values: List[str] = None,
    ):
        # The property code.
        self.attribute_code = attribute_code
        # The display name of the property.
        self.attribute_name = attribute_name
        # Indicates whether the property is required.
        self.required = required
        # The list of property values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_code is not None:
            result['AttributeCode'] = self.attribute_code

        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.required is not None:
            result['Required'] = self.required

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeCode') is not None:
            self.attribute_code = m.get('AttributeCode')

        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

