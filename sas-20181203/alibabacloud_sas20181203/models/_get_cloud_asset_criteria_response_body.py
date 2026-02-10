# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCloudAssetCriteriaResponseBody(DaraModel):
    def __init__(
        self,
        criteria_list: List[main_models.GetCloudAssetCriteriaResponseBodyCriteriaList] = None,
        request_id: str = None,
    ):
        # An array consisting of the information about the filter conditions that are used to search for cloud assets.
        self.criteria_list = criteria_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.criteria_list:
            for v1 in self.criteria_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CriteriaList'] = []
        if self.criteria_list is not None:
            for k1 in self.criteria_list:
                result['CriteriaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria_list = []
        if m.get('CriteriaList') is not None:
            for k1 in m.get('CriteriaList'):
                temp_model = main_models.GetCloudAssetCriteriaResponseBodyCriteriaList()
                self.criteria_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudAssetCriteriaResponseBodyCriteriaList(DaraModel):
    def __init__(
        self,
        multi_values: str = None,
        name: str = None,
        type: str = None,
        values: str = None,
    ):
        # The structured attribute values of the assets that match the keyword. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **vendor**: providers
        # *   **regionIds**: IDs of supported regions
        self.multi_values = multi_values
        # The name of the filter condition. Valid values:
        # 
        # *   **instanceId**: the ID of the instance
        # *   **instanceName**: the name of an instance
        # *   **internetIp**: the public IP address
        # *   **riskStatus**: the risk status
        # *   **vendorRegionId**: the region ID by service provider
        self.name = name
        # The type of the filter condition. Valid values:
        # 
        # *   **input**: The filter condition needs to be specified.
        # *   **select**: The filter condition is an option that can be selected from the drop-down list.
        self.type = type
        # The values of the search condition. This parameter is returned only if the value of **Type** is **select**.
        # 
        # >  If the value of **Type** is **input**, the value of this parameter is an empty string.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.multi_values is not None:
            result['MultiValues'] = self.multi_values

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultiValues') is not None:
            self.multi_values = m.get('MultiValues')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

