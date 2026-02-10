# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCanFixVulListRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        current_page: int = None,
        dealed: str = None,
        digest: str = None,
        image: str = None,
        instance_id: str = None,
        name: str = None,
        namespace: str = None,
        necessity: str = None,
        page_size: int = None,
        pod: str = None,
        region_id: str = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_region_id: str = None,
        scan_range: List[str] = None,
        status_list: str = None,
        tag: str = None,
        type: str = None,
        uuids: str = None,
    ):
        # The alias of the vulnerability that is specified in Common Vulnerabilities and Exposures (CVE).
        self.alias_name = alias_name
        # The cluster ID.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The container ID.
        self.container_id = container_id
        # The page number. Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # Specifies whether the vulnerability is handled. Valid values:
        # 
        # **y**: The vulnerability is handled. **n**: The vulnerability is not handled.
        self.dealed = dealed
        # The unique identifier of the image.
        self.digest = digest
        # The name of the image.
        self.image = image
        # The ID of the container image.
        # 
        # >  You can call the [ListRepository](https://help.aliyun.com/document_detail/451339.html) operation of Container Registry and obtain the ID of the container image from **InstanceId** in the response.
        self.instance_id = instance_id
        # The name of the vulnerability.
        self.name = name
        # The namespace of the cluster.
        # 
        # >  You can call the [GetOpaClusterNamespaceList](~~GetOpaClusterNamespaceList~~) operation to query the namespaces of clusters.
        self.namespace = namespace
        # The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values:
        # 
        # *   **asap**: high
        # *   **later**: medium
        # *   **nntf**: low
        self.necessity = necessity
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The name of the container group.
        self.pod = pod
        # The region ID of the image repository. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore
        # *   **ap-southeast-5**: Indonesia (Jakarta)
        # *   **us-east-1**: US (Virginia)
        # *   **us-west-1**: US (Silicon Valley)
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **eu-west-1**: UK (London)
        self.region_id = region_id
        # The ID of the image repository.
        # 
        # >  You can call the [ListRepository](https://help.aliyun.com/document_detail/145293.html) operation of Container Registry and obtain the ID of the image repository from **RepoId** in the response.
        self.repo_id = repo_id
        # The ID of the container image.
        # 
        # >  You can call the [ListRepository](https://help.aliyun.com/document_detail/451339.html) operation of Container Registry and obtain the ID of the container image from **InstanceId** in the response.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        # 
        # >  Fuzzy match is supported.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        # 
        # >  Fuzzy match is supported.
        self.repo_namespace = repo_namespace
        # The region ID of the image repository. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore
        # *   **ap-southeast-5**: Indonesia (Jakarta)
        # *   **us-east-1**: US (Virginia)
        # *   **us-west-1**: US (Silicon Valley)
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **eu-west-1**: UK (London)
        self.repo_region_id = repo_region_id
        # The type of the asset that you want to scan. Valid values:
        # 
        # *   **image**
        # *   **container**
        self.scan_range = scan_range
        # The status of the vulnerability. Valid values:
        # 
        # *   **1**: The vulnerability is unfixed.
        # *   **4**: The vulnerability is being fixed.
        # *   **7**:The vulnerability is fixed.
        self.status_list = status_list
        # The tag to add to the image.
        self.tag = tag
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: system vulnerability
        # *   **sca**: application vulnerability
        # 
        # This parameter is required.
        self.type = type
        # The UUID of the image. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.image is not None:
            result['Image'] = self.image

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type is not None:
            result['Type'] = self.type

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

