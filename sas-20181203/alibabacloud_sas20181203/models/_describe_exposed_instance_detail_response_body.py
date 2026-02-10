# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeExposedInstanceDetailResponseBody(DaraModel):
    def __init__(
        self,
        exposed_chains: List[main_models.DescribeExposedInstanceDetailResponseBodyExposedChains] = None,
        request_id: str = None,
    ):
        # The list of exposure details of the server or database.
        self.exposed_chains = exposed_chains
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.exposed_chains:
            for v1 in self.exposed_chains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExposedChains'] = []
        if self.exposed_chains is not None:
            for k1 in self.exposed_chains:
                result['ExposedChains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exposed_chains = []
        if m.get('ExposedChains') is not None:
            for k1 in m.get('ExposedChains'):
                temp_model = main_models.DescribeExposedInstanceDetailResponseBodyExposedChains()
                self.exposed_chains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeExposedInstanceDetailResponseBodyExposedChains(DaraModel):
    def __init__(
        self,
        all_vul_list: List[main_models.DescribeExposedInstanceDetailResponseBodyExposedChainsAllVulList] = None,
        cspm_risk_list: List[main_models.DescribeExposedInstanceDetailResponseBodyExposedChainsCspmRiskList] = None,
        exposure_component: str = None,
        exposure_ip: str = None,
        exposure_port: str = None,
        exposure_type: str = None,
        exposure_type_id: str = None,
        group_no: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        real_vul_list: List[main_models.DescribeExposedInstanceDetailResponseBodyExposedChainsRealVulList] = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # The information about all vulnerabilities on the server.
        self.all_vul_list = all_vul_list
        # The list of configuration risks.
        self.cspm_risk_list = cspm_risk_list
        # The server component that is exposed on the Internet.
        self.exposure_component = exposure_component
        # The IP address of the server or the public endpoint of the database.
        self.exposure_ip = exposure_ip
        # The port that is exposed on the Internet.
        self.exposure_port = exposure_port
        # The resource from which the server or database is exposed. Valid values:
        # 
        # *   **INTERNET_IP**: the public IP address of an Elastic Compute Service (ECS) instance.
        # *   **SLB**: the public IP address of a Server Load Balancer (SLB) instance.
        # *   **EIP**: an elastic IP address (EIP).
        # *   **DNAT**: the Network Address Translation (NAT) gateway that connects to the Internet by using the Destination Network Address Translation (DNAT) feature
        # *   **DB_CONNECTION**: the public endpoint of a database.
        self.exposure_type = exposure_type
        # The ID of the instance to which the resource belongs. The valid values of this parameter vary based on the value of the ExposureType parameter.
        # 
        # *   If the value of the ExposureType parameter is **INTERNET_IP**, this parameter is empty.
        # *   If the value of the ExposureType parameter is **SLB**, the value of this parameter is the ID of the SLB instance.
        # *   If the value of the ExposureType parameter is **EIP**, the value of this parameter is the ID of the EIP.
        # *   If the value of the ExposureType parameter is **DNAT**, the value of this parameter is the ID of the NAT gateway.
        # *   If the value of the ExposureType parameter is **DB_CONNECTION**, the value of this parameter is the ID of the database.
        self.exposure_type_id = exposure_type_id
        # The server group to which the server belongs.
        self.group_no = group_no
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The information about the vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.real_vul_list = real_vul_list
        # The region ID.
        # 
        # >  For information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The UUID of the server or the instance ID of the database.
        self.uuid = uuid

    def validate(self):
        if self.all_vul_list:
            for v1 in self.all_vul_list:
                 if v1:
                    v1.validate()
        if self.cspm_risk_list:
            for v1 in self.cspm_risk_list:
                 if v1:
                    v1.validate()
        if self.real_vul_list:
            for v1 in self.real_vul_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllVulList'] = []
        if self.all_vul_list is not None:
            for k1 in self.all_vul_list:
                result['AllVulList'].append(k1.to_map() if k1 else None)

        result['CspmRiskList'] = []
        if self.cspm_risk_list is not None:
            for k1 in self.cspm_risk_list:
                result['CspmRiskList'].append(k1.to_map() if k1 else None)

        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component

        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip

        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port

        if self.exposure_type is not None:
            result['ExposureType'] = self.exposure_type

        if self.exposure_type_id is not None:
            result['ExposureTypeId'] = self.exposure_type_id

        if self.group_no is not None:
            result['GroupNo'] = self.group_no

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        result['RealVulList'] = []
        if self.real_vul_list is not None:
            for k1 in self.real_vul_list:
                result['RealVulList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_vul_list = []
        if m.get('AllVulList') is not None:
            for k1 in m.get('AllVulList'):
                temp_model = main_models.DescribeExposedInstanceDetailResponseBodyExposedChainsAllVulList()
                self.all_vul_list.append(temp_model.from_map(k1))

        self.cspm_risk_list = []
        if m.get('CspmRiskList') is not None:
            for k1 in m.get('CspmRiskList'):
                temp_model = main_models.DescribeExposedInstanceDetailResponseBodyExposedChainsCspmRiskList()
                self.cspm_risk_list.append(temp_model.from_map(k1))

        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')

        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')

        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')

        if m.get('ExposureType') is not None:
            self.exposure_type = m.get('ExposureType')

        if m.get('ExposureTypeId') is not None:
            self.exposure_type_id = m.get('ExposureTypeId')

        if m.get('GroupNo') is not None:
            self.group_no = m.get('GroupNo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        self.real_vul_list = []
        if m.get('RealVulList') is not None:
            for k1 in m.get('RealVulList'):
                temp_model = main_models.DescribeExposedInstanceDetailResponseBodyExposedChainsRealVulList()
                self.real_vul_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeExposedInstanceDetailResponseBodyExposedChainsRealVulList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        name: str = None,
        necessity: str = None,
        type: str = None,
        uuid: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The name of the vulnerability.
        self.name = name
        # The priority to fix the vulnerability. Valid values:
        # 
        # *   **asap**: high
        # *   **later**: medium
        # *   **nntf**: low
        # 
        # >  We recommend that you fix the vulnerabilities that have the **high** priority at the earliest opportunity.
        self.necessity = necessity
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerabilities
        # *   **sys**: Windows system vulnerabilities
        # *   **cms**: Web-CMS vulnerabilities
        # *   **app**: application vulnerabilities
        # *   **emg**: urgent vulnerabilities
        # *   **sca**: middleware vulnerabilities
        self.type = type
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.name is not None:
            result['Name'] = self.name

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeExposedInstanceDetailResponseBodyExposedChainsCspmRiskList(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_sub_type_name: str = None,
        asset_type: int = None,
        asset_type_name: str = None,
        check_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        risk_level: str = None,
        vendor: int = None,
    ):
        # The subtype of the cloud asset. Valid values:
        # 
        # *   **0**: Elastic Compute Service (ECS).
        # 
        #     *   **100**: instance.
        # 
        # *   **3**: ApsaraDB RDS.
        # 
        #     *   **0**: instance.
        # 
        # *   **4**: ApsaraDB for MongoDB (MongoDB).
        # 
        #     *   **0**: instance.
        # 
        # *   **5**: ApsaraDB for Redis (Redis).
        # 
        #     *   **0**: instance.
        self.asset_sub_type = asset_sub_type
        # The subtype name of the cloud asset. Valid values:
        # 
        # *   **INSTANCE**: MongoDB instance, Apsara DB for RDS instance, and ApsaraDB for Redis instance.
        # *   **ECS_INSTANCE**: ECS instance.
        self.asset_sub_type_name = asset_sub_type_name
        # The instance type. Valid values:
        # 
        # *   0: an ECS instance.
        # *   3: an ApsaraDB RDS instance.
        # *   4: an ApsaraDB for MongoDB instance.
        # *   5: an ApsaraDB for Redis instance.
        self.asset_type = asset_type
        # The name of the cloud asset type. Valid values:
        # 
        # *   **ECS**
        # *   **RDS**
        # *   **KVSTORE**
        # *   **MONGODB**
        self.asset_type_name = asset_type_name
        # The name of the check item.
        self.check_name = check_name
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The risk level. Valid values:
        # 
        # *   **HIGH**
        # *   **MEDIUM**
        # *   **LOW**
        self.risk_level = risk_level
        # The type of the cloud asset by source. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_sub_type_name is not None:
            result['AssetSubTypeName'] = self.asset_sub_type_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.asset_type_name is not None:
            result['AssetTypeName'] = self.asset_type_name

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetSubTypeName') is not None:
            self.asset_sub_type_name = m.get('AssetSubTypeName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AssetTypeName') is not None:
            self.asset_type_name = m.get('AssetTypeName')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class DescribeExposedInstanceDetailResponseBodyExposedChainsAllVulList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        name: str = None,
        necessity: str = None,
        type: str = None,
        uuid: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The name of the vulnerability.
        self.name = name
        # The priority to fix the vulnerability. Valid values:
        # 
        # *   **asap**: high
        # *   **later**: medium
        # *   **nntf**: low
        # 
        # >  We recommend that you fix the vulnerabilities that have the **high** priority at the earliest opportunity.
        self.necessity = necessity
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerabilities
        # *   **sys**: Windows system vulnerabilities
        # *   **cms**: Web-CMS vulnerabilities
        # *   **app**: application vulnerabilities
        # *   **emg**: urgent vulnerabilities
        # *   **sca**: middleware vulnerabilities
        self.type = type
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.name is not None:
            result['Name'] = self.name

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

