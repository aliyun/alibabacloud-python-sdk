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
        # List of asset query condition information.
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
        #  - **internetIp**: Public IP Address. 
        #  - **intranetIp**: Private IP Address.
        #  - **instanceName**: Instance Name.
        #  - **instanceId**: Instance ID. 
        #  - **machineType**: Instance Type. 
        #  - **clusterIdList**: Cluster ID list. 
        #  - **vpcInstanceId**: VPC ID. 
        #  - **osName**: OS. 
        #  - **osType**: OS type. 
        #  - **hcStatus**: Whether Baseline Risk Exists. 
        #  - **vulStatus**: Whether Vulnerability Exists. 
        #  - **asapVulStatus**: Whether there is an urgent vulnerability. 
        #  - **alarmStatus**: Whether Alert Exists. 
        #  - **riskStatus**: Whether there is a risk. 
        #  - **clientStatus**: Whether it is online. 
        #  - **clientSubStatus**: Client sub-status. 
        #  - **runningStatus**: Power-on status. 
        #  - **tagName**: Tag name. 
        #  - **vendorAuthAlias**: Authorized account remarks. 
        #  - **vendorUid**: Authorized account ID. 
        #  - **vendorUserName**: Authorized account name. 
        #  - **namespace**: Namespace. 
        #  - **appName**: Application name. 
        #  - **groupName**: Group name. 
        #  - **regionId**: Region. 
        #  - **groupId**: Group ID. 
        #  - **newInstance**: Whether it is a new asset. 
        #  - **containerStatus**: Whether there is a container. 
        #  - **importance**: Asset importance. 
        #  - **exposedStatus**: Whether it is an exposed server. 
        #  - **clusterId**: Cluster ID. 
        #  - **authVersion**: Authorization version. 
        #  - **flag**: Cloud provider. 
        #  - **ipList**: IP list. 
        #  - **uuidList**: UUID. 
        #  - **aiStatus**: Whether there is an AI component. 
        #  - **tagKeyValue**: ECS tag. 
        #  - **ecsType**: Server type. 
        #  - **alisecguardStatus**: Self-protection status. 
        #  - **alihipsStatus**: AliHips status. 
        #  - **alinetStatus**: AliNet status. 
        #  - **alidetectStatus**: Endpoint engine status. 
        #  - **yundunMonitorStatus**: Information collection component status. 
        #  - **clusterNodeStatus**: Whether it is a cluster node.
        self.name = name
        # The type of the search condition. Valid values:
        # 
        # *   **input**: The search condition needs to be specified.
        # *   **select**: The search condition is an option that can be selected from the drop-down list.
        self.type = type
        # The attribute values of the assets that match the keyword.
        # > - When **Name** is **machineType**, the enum values are: 
        # >>- **38**: Elastic Container Instance. 
        # >>- **51**: RunD Container Instance. 
        # >>- **52**: RunC Container Instance. 
        # >- When **Name** is **osType**, the enum values are: 
        # >>- **linux**: Linux. 
        # >>- **windows**: Windows. 
        # >- When **Name** is **hcStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >- When **Name** is **vulStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >- When **Name** is **asapVulStatus**, the enum values are: 
        # >>- **NO**: No.
        # >>- **YES**: Yes. 
        # >- When **Name** is **alarmStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >- When **Name** is **riskStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >>- **UNKNOWN**: Unknown. 
        # >- When **Name** is **clientStatus**, the enum values are: 
        # >>- **online**: Online. 
        # >>- **offline**: Offline. 
        # >>- **pause**: Protection Suspended. 
        # >- When **Name** is **clientSubStatus**, the enum values are: 
        # >>- **online**: Online. 
        # >>- **offline**: Offline. 
        # >>- **pause**: Protection Suspended. 
        # >>- **stopped**: Server Shutdown. 
        # >>- **uninstalled**: Not Installed. 
        # >- When **Name** is **runningStatus**, the enum values are: 
        # >>- **Running**: On. 
        # >>- **notRunning**: Off. 
        # >>- **UNKNOWN**: Unknown. 
        # >- When **Name** is **importance**, the enum values are: 
        # >>- **important**: Important. 
        # >>- **general**: Normal. 
        # >>- **test**: Test. 
        # >- When **Name** is **containerStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >- When **Name** is **exposedStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >- When **Name** is **authVersion**, the enum values are: 
        # >>- **1**: Basic. 
        # >>- **3**: Enterprise. 
        # >>- **5**: Advanced.
        # >>- **6**: Anti-virus. 
        # >>- **7**: Ultimate. 
        # >- When **Name** is **flag**, the enum values are: 
        # >>- **0|8|15**: Alibaba Cloud. 
        # >>- **1**: External Host. 
        # >>- **2**: IDC. 
        # >>- **3**: Tencent Cloud. 
        # >>- **4**: Huawei Cloud. 
        # >>- **5**: Azure. 
        # >>- **7**: AWS. 
        # >>- **9**: SAE. 
        # >>- **10**: PAI. 
        # >>- **13**: ACS. 
        # >>- **14**: Volcano Cloud. 
        # >>- **16**: Google Cloud. 
        # >- When **Name** is **aiStatus**, the enum values are: 
        # >>- **NO**: No. 
        # >>- **YES**: Yes. 
        # >- When **Name** is **ecsType**, the enum values are: 
        # >>- **8**: Simple Application Server. 
        # >>- **11**: LINGJUN GPU-accelerated Bare Metal Instance. 
        # >>- **15**: RDS Custom. 
        # >>- **!8**: Host. 
        # >- When **Name** is **alisecguardStatus**, the enum values are: 
        # >>- **0**: Plug-in Online. 
        # >>- **1**: Plug-in Disabled. 
        # >>- **2**: Plug-in Offline. 
        # >>- **-99**: The installation failed. 
        # >- When **Name** is **alihipsStatus**, the enum values are: 
        # >>- **0**: Plug-in Online. 
        # >>- **1**: Plug-in Disabled. 
        # >>- **2**: Plug-in Offline. 
        # >>- **-99**: The installation failed. 
        # >- When **Name** is **alinetStatus**, the enum values are: 
        # >>- **0**: Plug-in Online. 
        # >>- **1**: Plug-in Disabled. 
        # >>- **2**: Plug-in Offline. 
        # >>- **-99**: The installation failed. 
        # >- When **Name** is **alidetectStatus**, the enum values are: 
        # >>- **0**: Plug-in Online. 
        # >>- **1**: Plug-in Disabled. 
        # >>- **2**: Plug-in Offline. 
        # >>- **-99**: The installation failed. 
        # >- When **Name** is **yundunMonitorStatus**, the enum values are: 
        # >>- **0**: Plug-in Online. 
        # >>- **1**: Plug-in Disabled. 
        # >>- **2**: Plug-in Offline. 
        # >>- **-99**: The installation failed. 
        # >- When **Name** is **clusterNodeStatus**, the enum values are: 
        # >>- **false**: No. 
        # >>- **true**: Yes.
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

