# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vul_records: List[main_models.DescribeVulListResponseBodyVulRecords] = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The value of NextToken that is returned when the NextToken method is used.
        self.next_token = next_token
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of vulnerabilities returned.
        self.total_count = total_count
        # The information about the vulnerability.
        self.vul_records = vul_records

    def validate(self):
        if self.vul_records:
            for v1 in self.vul_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VulRecords'] = []
        if self.vul_records is not None:
            for k1 in self.vul_records:
                result['VulRecords'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k1 in m.get('VulRecords'):
                temp_model = main_models.DescribeVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k1))

        return self

class DescribeVulListResponseBodyVulRecords(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        auth_version: str = None,
        bind: bool = None,
        container_id: str = None,
        extend_content_json: main_models.DescribeVulListResponseBodyVulRecordsExtendContentJson = None,
        first_ts: int = None,
        group_id: int = None,
        image: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        k_8s_cluster_id: str = None,
        k_8s_namespace: str = None,
        k_8s_node_id: str = None,
        k_8s_node_name: str = None,
        k_8s_pod_name: str = None,
        last_ts: int = None,
        modify_ts: int = None,
        name: str = None,
        namespace: str = None,
        necessity: str = None,
        online: bool = None,
        os_name: str = None,
        os_version: str = None,
        primary_id: int = None,
        progress: int = None,
        rasp_defend: int = None,
        rasp_status: int = None,
        real_risk: bool = None,
        region_id: str = None,
        related: str = None,
        repair_ts: int = None,
        result_code: str = None,
        result_message: str = None,
        rule_tag: str = None,
        status: int = None,
        tag: str = None,
        type: str = None,
        uuid: str = None,
    ):
        # The name of the vulnerability.
        self.alias_name = alias_name
        # The edition of Security Center that is authorized to scan the asset. Valid values:
        # 
        # *   **1**: Basic.
        # *   **6**: Anti-virus.
        # *   **5**: Advanced.
        # *   **3**: Enterprise.
        # *   **7**: Ultimate.
        # *   **10**: Value-added Plan.
        self.auth_version = auth_version
        # Indicates whether Security Center is authorized to scan the asset. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.bind = bind
        # The container ID.
        self.container_id = container_id
        # The extended information about the vulnerability.
        self.extend_content_json = extend_content_json
        # The timestamp when the vulnerability was first detected. Unit: milliseconds.
        self.first_ts = first_ts
        # The ID of the asset group.
        self.group_id = group_id
        # The name of the image.
        self.image = image
        # The ID of the asset.
        self.instance_id = instance_id
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the asset.
        self.internet_ip = internet_ip
        # The private IP address of the asset.
        self.intranet_ip = intranet_ip
        # The ID of the cluster.
        # 
        # >  The value of this parameter is returned only if you use the Ultimate edition of Security Center that can protect container assets.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The namespace.
        # 
        # >  If you use the Ultimate edition of Security Center, the value of this parameter is queried from container assets. If you do not use the Ultimate edition, the value of this parameter is queried from the Security Center agent.
        self.k_8s_namespace = k_8s_namespace
        # The ID of the node.
        # 
        # >  The value of this parameter is returned only if you use the Ultimate edition of Security Center that can protect container assets.
        self.k_8s_node_id = k_8s_node_id
        # The name of the node.
        # 
        # >  The value of this parameter is returned only if you use the Ultimate edition of Security Center that can protect container assets.
        self.k_8s_node_name = k_8s_node_name
        # The name of the pod.
        # 
        # >  The value of this parameter is returned only if you use the Ultimate edition of Security Center that can protect container assets.
        self.k_8s_pod_name = k_8s_pod_name
        # The timestamp when the vulnerability was last detected. Unit: milliseconds.
        self.last_ts = last_ts
        # The timestamp when the vulnerability status was modified. Unit: milliseconds.
        self.modify_ts = modify_ts
        # The name of the vulnerability.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The priority to fix the vulnerability. Valid values:
        # 
        # *   **asap**: high.
        # *   **later**: medium.
        # *   **nntf**: low.
        # 
        # >  We recommend that you fix **high-risk** vulnerabilities at the earliest opportunity.
        self.necessity = necessity
        # Indicates whether the Security Center agent on the asset is online. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.online = online
        # The name of the operating system for your asset.
        self.os_name = os_name
        # The name of the operating system for your asset.
        self.os_version = os_version
        # The ID of the vulnerability.
        self.primary_id = primary_id
        # The progress of the vulnerability fixing.
        self.progress = progress
        # Indicates whether the application protection feature is supported. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        # 
        # >  If this parameter is not returned, the application protection feature is not supported.
        self.rasp_defend = rasp_defend
        # The protection mode of the application protection feature. Valid values:
        # 
        # *   **0**: unprotected.
        # *   **1**: the Monitor mode.
        # *   **2**: the Block mode.
        # *   **3**: disabled.
        self.rasp_status = rasp_status
        # Indicates whether the vulnerability is easily exploited. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.real_risk = real_risk
        # The region ID of the asset.
        self.region_id = region_id
        # The Common Vulnerabilities and Exposures (CVE) IDs related to the vulnerability. Multiple CVE IDs are separated by commas (,).
        self.related = related
        # The timestamp when the vulnerability was fixed. Unit: milliseconds. This parameter is returned only if you fix vulnerabilities in the Security Center console.
        self.repair_ts = repair_ts
        # The code that indicates the vulnerability fixing result.
        self.result_code = result_code
        # The message that indicates the vulnerability fixing result.
        self.result_message = result_message
        # The tag of this vulnerability. Valid values:
        # 
        # *   **AI**: AI-related components.
        self.rule_tag = rule_tag
        # The status of the vulnerability. Valid values:
        # 
        # *   **1**: unfixed.
        # *   **2**: fix failed.
        # *   **3**: rollback failed.
        # *   **4**: being fixed.
        # *   **5**: being rolled back.
        # *   **6**: being verified.
        # *   **7**: fixed.
        # *   **8**: fixed and to be restarted.
        # *   **9**: rolled back.
        # *   **10**: ignored.
        # *   **11**: rolled back and to be restarted.
        # *   **12**: not found.
        # *   **20**: expired.
        self.status = status
        # The tag that is added to the vulnerability.
        self.tag = tag
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability.
        # *   **sys**: Windows system vulnerability.
        # *   **cms**: Web-CMS vulnerability.
        # *   **emg**: urgent vulnerability.
        # *   **app**: application vulnerability.
        # *   **sca**: application vulnerability that is detected by using software component analysis.
        self.type = type
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        if self.extend_content_json:
            self.extend_content_json.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()

        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image is not None:
            result['Image'] = self.image

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id

        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name

        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name

        if self.last_ts is not None:
            result['LastTs'] = self.last_ts

        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.online is not None:
            result['Online'] = self.online

        if self.os_name is not None:
            result['OsName'] = self.os_name

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.rasp_status is not None:
            result['RaspStatus'] = self.rasp_status

        if self.real_risk is not None:
            result['RealRisk'] = self.real_risk

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.related is not None:
            result['Related'] = self.related

        if self.repair_ts is not None:
            result['RepairTs'] = self.repair_ts

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ExtendContentJson') is not None:
            temp_model = main_models.DescribeVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m.get('ExtendContentJson'))

        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')

        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')

        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')

        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')

        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('RaspStatus') is not None:
            self.rasp_status = m.get('RaspStatus')

        if m.get('RealRisk') is not None:
            self.real_risk = m.get('RealRisk')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Related') is not None:
            self.related = m.get('Related')

        if m.get('RepairTs') is not None:
            self.repair_ts = m.get('RepairTs')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeVulListResponseBodyVulRecordsExtendContentJson(DaraModel):
    def __init__(
        self,
        absolute_path: str = None,
        alias_name: str = None,
        description: str = None,
        emg_proof: str = None,
        ip: str = None,
        last_ts: int = None,
        necessity: main_models.DescribeVulListResponseBodyVulRecordsExtendContentJsonNecessity = None,
        os: str = None,
        os_release: str = None,
        primary_id: int = None,
        rpm_entity_list: List[main_models.DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList] = None,
        status: str = None,
        tag: str = None,
        target: str = None,
        cve_list: List[str] = None,
    ):
        # The path to the package of the software that has the vulnerability.
        self.absolute_path = absolute_path
        # The name of the vulnerability.
        self.alias_name = alias_name
        # The description of the vulnerability.
        self.description = description
        # The returned message that indicates the urgent vulnerability.
        self.emg_proof = emg_proof
        # The public IP address of the asset that is associated with the vulnerability.
        self.ip = ip
        # The timestamp when the vulnerability was last detected. Unit: milliseconds.
        self.last_ts = last_ts
        # Indicates whether the vulnerability needs to be fixed.
        self.necessity = necessity
        # The name of the operating system.
        self.os = os
        # The information about the operating system version.
        self.os_release = os_release
        # The ID of the vulnerability.
        self.primary_id = primary_id
        # The information about RPM Package Manager (RPM) packages.
        self.rpm_entity_list = rpm_entity_list
        # The status of the vulnerability. Valid values:
        # 
        # *   **1**: unfixed.
        # *   **2**: fix failed.
        # *   3: rollback failed.
        # *   **4**: being fixed.
        # *   **5**: being rolled back.
        # *   **6**: being verified.
        # *   **7**: fixed.
        # *   **8**: fixed and to be restarted.
        # *   **9**: rolled back.
        # *   **10**: ignored.
        # *   **11**: rolled back and to be restarted.
        # *   **12**: not found.
        # *   **20**: expired.
        self.status = status
        # The tag that is added to the vulnerability.
        self.tag = tag
        # The URL of the vulnerability.
        self.target = target
        # The CVE list.
        self.cve_list = cve_list

    def validate(self):
        if self.necessity:
            self.necessity.validate()
        if self.rpm_entity_list:
            for v1 in self.rpm_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.absolute_path is not None:
            result['AbsolutePath'] = self.absolute_path

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.description is not None:
            result['Description'] = self.description

        if self.emg_proof is not None:
            result['EmgProof'] = self.emg_proof

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.last_ts is not None:
            result['LastTs'] = self.last_ts

        if self.necessity is not None:
            result['Necessity'] = self.necessity.to_map()

        if self.os is not None:
            result['Os'] = self.os

        if self.os_release is not None:
            result['OsRelease'] = self.os_release

        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id

        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k1 in self.rpm_entity_list:
                result['RpmEntityList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.target is not None:
            result['Target'] = self.target

        if self.cve_list is not None:
            result['cveList'] = self.cve_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbsolutePath') is not None:
            self.absolute_path = m.get('AbsolutePath')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmgProof') is not None:
            self.emg_proof = m.get('EmgProof')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')

        if m.get('Necessity') is not None:
            temp_model = main_models.DescribeVulListResponseBodyVulRecordsExtendContentJsonNecessity()
            self.necessity = temp_model.from_map(m.get('Necessity'))

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsRelease') is not None:
            self.os_release = m.get('OsRelease')

        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')

        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k1 in m.get('RpmEntityList'):
                temp_model = main_models.DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('cveList') is not None:
            self.cve_list = m.get('cveList')

        return self

class DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(DaraModel):
    def __init__(
        self,
        container_name: str = None,
        extend_field: str = None,
        full_version: str = None,
        image_name: str = None,
        match_detail: str = None,
        match_list: List[str] = None,
        name: str = None,
        path: str = None,
        pid: str = None,
        update_cmd: str = None,
        version: str = None,
    ):
        # The name of the container.
        self.container_name = container_name
        # The extended information about the software package that has the vulnerability.
        self.extend_field = extend_field
        # The complete version number.
        self.full_version = full_version
        # The name of the image.
        self.image_name = image_name
        # The reason why the vulnerability is detected.
        self.match_detail = match_detail
        # The rules that are used to detect the vulnerability.
        self.match_list = match_list
        # The name of the RPM package.
        self.name = name
        # The path to the software that has the vulnerability.
        self.path = path
        # The process ID.
        self.pid = pid
        # The command that is used to fix the vulnerability.
        self.update_cmd = update_cmd
        # The version number of the package of the software that has the vulnerability.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.extend_field is not None:
            result['ExtendField'] = self.extend_field

        if self.full_version is not None:
            result['FullVersion'] = self.full_version

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail

        if self.match_list is not None:
            result['MatchList'] = self.match_list

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('ExtendField') is not None:
            self.extend_field = m.get('ExtendField')

        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')

        if m.get('MatchList') is not None:
            self.match_list = m.get('MatchList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeVulListResponseBodyVulRecordsExtendContentJsonNecessity(DaraModel):
    def __init__(
        self,
        assets_factor: str = None,
        cvss_factor: str = None,
        enviroment_factor: str = None,
        is_calc: str = None,
        status: str = None,
        time_factor: str = None,
        total_score: str = None,
    ):
        # The asset importance score. Valid values:
        # 
        # *   **2**: important asset.
        # *   **1**: common asset.
        # *   **0**: test asset.
        self.assets_factor = assets_factor
        # The Common Vulnerability Scoring System (CVSS) score.
        self.cvss_factor = cvss_factor
        # The environment score.
        self.enviroment_factor = enviroment_factor
        # Indicates whether the vulnerability priority score is calculated. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.is_calc = is_calc
        # The status of the vulnerability priority score. Valid values:
        # 
        # *   **none**: No score is generated.
        # *   **pending**: The score is pending calculation.
        # *   **normal**: The calculation is normal.
        self.status = status
        # The time score.
        self.time_factor = time_factor
        # The vulnerability priority score.
        # 
        # The following list describes scores and related fixing suggestions:
        # 
        # *   If the score is from **13.5 to 15**, the vulnerability is a high-risk vulnerability. You must fix the vulnerability at the earliest opportunity.
        # *   If the score is **greater than or equal to 7 but less than 13.5**, the vulnerability is a medium-risk vulnerability. You can fix the vulnerability at your convenience.
        # *   If the score is **less than 7**, the vulnerability is a low-risk vulnerability. You can ignore the vulnerability.
        self.total_score = total_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_factor is not None:
            result['Assets_factor'] = self.assets_factor

        if self.cvss_factor is not None:
            result['Cvss_factor'] = self.cvss_factor

        if self.enviroment_factor is not None:
            result['Enviroment_factor'] = self.enviroment_factor

        if self.is_calc is not None:
            result['Is_calc'] = self.is_calc

        if self.status is not None:
            result['Status'] = self.status

        if self.time_factor is not None:
            result['Time_factor'] = self.time_factor

        if self.total_score is not None:
            result['Total_score'] = self.total_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assets_factor') is not None:
            self.assets_factor = m.get('Assets_factor')

        if m.get('Cvss_factor') is not None:
            self.cvss_factor = m.get('Cvss_factor')

        if m.get('Enviroment_factor') is not None:
            self.enviroment_factor = m.get('Enviroment_factor')

        if m.get('Is_calc') is not None:
            self.is_calc = m.get('Is_calc')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Time_factor') is not None:
            self.time_factor = m.get('Time_factor')

        if m.get('Total_score') is not None:
            self.total_score = m.get('Total_score')

        return self

