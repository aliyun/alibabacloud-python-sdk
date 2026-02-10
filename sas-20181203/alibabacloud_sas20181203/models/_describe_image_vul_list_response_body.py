# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageVulListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vul_records: List[main_models.DescribeImageVulListResponseBodyVulRecords] = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of vulnerabilities returned.
        self.total_count = total_count
        # An array that consists of the vulnerabilities.
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

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k1 in m.get('VulRecords'):
                temp_model = main_models.DescribeImageVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k1))

        return self

class DescribeImageVulListResponseBodyVulRecords(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        can_fix: str = None,
        can_update: bool = None,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        extend_content_json: main_models.DescribeImageVulListResponseBodyVulRecordsExtendContentJson = None,
        first_ts: int = None,
        image: str = None,
        image_digest: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_ts: int = None,
        layers: List[str] = None,
        malicious_source: str = None,
        modify_ts: int = None,
        name: str = None,
        namespace: str = None,
        necessity: str = None,
        pod: str = None,
        primary_id: int = None,
        related: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        rule_tag: str = None,
        scan_time: int = None,
        status: int = None,
        tag: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        type: str = None,
        uuid: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # Indicates whether the vulnerability can be fixed in the Security Center console. Valid values:
        # 
        # *   **yes**: yes
        # *   **no**: no
        self.can_fix = can_fix
        # Indicates whether the package of the software that has the vulnerability can be upgraded by using Security Center. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.can_update = can_update
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the container.
        self.container_id = container_id
        # The extended information about the vulnerability.
        self.extend_content_json = extend_content_json
        # The timestamp when the first scan was performed. Unit: milliseconds.
        self.first_ts = first_ts
        # The name of the image.
        self.image = image
        # The digest of the image.
        self.image_digest = image_digest
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.last_ts = last_ts
        # The image layers.
        self.layers = layers
        # The source of the malicious file. Valid values:
        # 
        # *   **agentless**: agentless detection
        # *   **image**: image
        # *   **container**: container
        self.malicious_source = malicious_source
        # The timestamp when the information about the vulnerability was updated. Unit: milliseconds.
        self.modify_ts = modify_ts
        # The name of the vulnerability.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The priority to fix the vulnerability. Valid values:
        # 
        # *   **asap**: high. You must fix the vulnerability at the earliest opportunity.
        # *   **later**: medium. You can fix the vulnerability based on your business requirements.
        # *   **nntf**: low. You can ignore the vulnerability.
        self.necessity = necessity
        # The pod.
        self.pod = pod
        # The ID of the vulnerability.
        self.primary_id = primary_id
        # The Common Vulnerabilities and Exposures (CVE) ID of the associated vulnerability.
        self.related = related
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The tag of this vulnerability. Valid values:
        # 
        # *   **AI**: AI-related components.
        self.rule_tag = rule_tag
        # The time at which the scan was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.scan_time = scan_time
        # The status of the vulnerability. Valid values:
        # 
        # *   **1**: unfixed
        # *   **7**: fixed
        self.status = status
        # The tag that is added to the image vulnerability.
        self.tag = tag
        # The ID of the asset on which the vulnerability is detected.
        self.target_id = target_id
        # The name of the asset on which the vulnerability is detected.
        self.target_name = target_name
        # The type of the asset on which the vulnerability is detected. Valid values:
        # 
        # *   **ECS_SNAPSHOT**: snapshot
        # *   **ECS_IMAGE**: image
        self.target_type = target_type
        # The type of the vulnerability. The value is fixed as CVE, which indicates image vulnerabilities.
        self.type = type
        # The UUID of the server.
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

        if self.can_fix is not None:
            result['CanFix'] = self.can_fix

        if self.can_update is not None:
            result['CanUpdate'] = self.can_update

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()

        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts

        if self.image is not None:
            result['Image'] = self.image

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_ts is not None:
            result['LastTs'] = self.last_ts

        if self.layers is not None:
            result['Layers'] = self.layers

        if self.malicious_source is not None:
            result['MaliciousSource'] = self.malicious_source

        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id

        if self.related is not None:
            result['Related'] = self.related

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag

        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CanFix') is not None:
            self.can_fix = m.get('CanFix')

        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ExtendContentJson') is not None:
            temp_model = main_models.DescribeImageVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m.get('ExtendContentJson'))

        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')

        if m.get('Layers') is not None:
            self.layers = m.get('Layers')

        if m.get('MaliciousSource') is not None:
            self.malicious_source = m.get('MaliciousSource')

        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')

        if m.get('Related') is not None:
            self.related = m.get('Related')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')

        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeImageVulListResponseBodyVulRecordsExtendContentJson(DaraModel):
    def __init__(
        self,
        os: str = None,
        os_release: str = None,
        rpm_entity_list: List[main_models.DescribeImageVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList] = None,
    ):
        # The name of the operating system.
        self.os = os
        # The version of the operating system in the image.
        self.os_release = os_release
        # The details of the package of the software that has the vulnerability.
        self.rpm_entity_list = rpm_entity_list

    def validate(self):
        if self.rpm_entity_list:
            for v1 in self.rpm_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.os is not None:
            result['Os'] = self.os

        if self.os_release is not None:
            result['OsRelease'] = self.os_release

        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k1 in self.rpm_entity_list:
                result['RpmEntityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsRelease') is not None:
            self.os_release = m.get('OsRelease')

        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k1 in m.get('RpmEntityList'):
                temp_model = main_models.DescribeImageVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k1))

        return self

class DescribeImageVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(DaraModel):
    def __init__(
        self,
        full_version: str = None,
        layer: str = None,
        match_detail: str = None,
        match_list: List[str] = None,
        name: str = None,
        path: str = None,
        update_cmd: str = None,
        version: str = None,
    ):
        # The complete version number of the package.
        self.full_version = full_version
        # The SHA-256 value of the digest of the image layer.
        self.layer = layer
        # The reason why the vulnerability is detected.
        self.match_detail = match_detail
        # The details of the rule that is used to detect the vulnerability.
        self.match_list = match_list
        # The name of the software package.
        self.name = name
        # The path of the software that has the vulnerability.
        self.path = path
        # The command that is used to fix the vulnerability.
        self.update_cmd = update_cmd
        # The version number of the package.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_version is not None:
            result['FullVersion'] = self.full_version

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail

        if self.match_list is not None:
            result['MatchList'] = self.match_list

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')

        if m.get('MatchList') is not None:
            self.match_list = m.get('MatchList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

