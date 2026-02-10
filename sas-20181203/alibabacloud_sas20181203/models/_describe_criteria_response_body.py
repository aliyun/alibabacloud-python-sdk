# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCriteriaResponseBody(DaraModel):
    def __init__(
        self,
        criteria_list: List[main_models.DescribeCriteriaResponseBodyCriteriaList] = None,
        request_id: str = None,
    ):
        # The information about the search conditions of assets.
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
                temp_model = main_models.DescribeCriteriaResponseBodyCriteriaList()
                self.criteria_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCriteriaResponseBodyCriteriaList(DaraModel):
    def __init__(
        self,
        multi_values: str = None,
        name: str = None,
        type: str = None,
        values: str = None,
    ):
        # The structured attribute values of the assets that match the keyword. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **vendor**: providers.
        # *   **regionIds**: IDs of supported regions
        self.multi_values = multi_values
        # The name of the search condition. Valid values:
        # 
        # *   **internetIp**: the public IP address.
        # *   **intranetIp**: the private IP address.
        # *   **instanceName**: the name of the instance.
        # *   **instanceId**: the instance ID.
        # *   **vpcInstanceId**: The ID of the virtual private cloud (VPC) to which the instance belongs.
        # *   **osName**: the operating system.
        # *   **osType**: the operating system type.
        # *   **hcStatus**: indicates whether baseline risks exist.
        # *   **vulStatus**: indicates whether vulnerabilities exist.
        # *   **alarmStatus**: indicates whether security alerts exist.
        # *   **riskStatus**: indicates whether risks exist.
        # *   **clientStatus**: indicates the status of the client.
        # *   **runningStatus**: the running status of the asset.
        # *   **tagName**: the name of the tag.
        # *   **groupName**: the name of the server group.
        # *   **regionId**: the region ID.
        # *   **importance**: the importance of the asset.
        # *   **exposedStatus**: indicates whether the server is exposed.
        # *   **authVersion**: the authorization version.
        # *   **flag**: the cloud service provider.
        # *   **ipList**: the IP address list.
        # *   **uuidList** :the UUID.
        # *   **tagKeyValue**: the ECS tag.
        # *   **vendorAuthAlias**: the account name.
        self.name = name
        # The type of the search condition. Valid values:
        # 
        # *   **input**: The search condition needs to be specified.
        # *   **select**: The search condition is an option that can be selected from the drop-down list.
        self.type = type
        # The attribute values of the assets that match the keyword.
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

