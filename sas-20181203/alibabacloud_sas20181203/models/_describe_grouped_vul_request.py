# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupedVulRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        asset_type: str = None,
        attach_types: str = None,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: int = None,
        cve_id: str = None,
        dealed: str = None,
        group_id: str = None,
        lang: str = None,
        necessity: str = None,
        page_size: int = None,
        rasp_defend: int = None,
        resource_directory_account_id: int = None,
        search_tags: str = None,
        target_type: str = None,
        type: str = None,
        uuids: str = None,
    ):
        # The alias of the vulnerability to query.
        self.alias_name = alias_name
        # The Asset Type where the vulnerability is detected. Separate multiple types with commas (,). Valid values:
        # - **ECS**: host asset
        # - **CONTAINER**: container asset.
        self.asset_type = asset_type
        # The vulnerability type. This query condition is valid only for application vulnerabilities. Separate multiple values with commas (,). Valid values:
        # - **sca**: software constituency parsing vulnerability
        # - **app**: application vulnerability.
        self.attach_types = attach_types
        # The cluster ID.
        self.cluster_id = cluster_id
        # The container search field. Valid values:
        # 
        # - **instanceId**: instance ID
        # - **appName**: application name
        # - **clusterId**: cluster ID
        # - **regionId**: region
        # - **nodeName**: node name
        # - **namespace**: namespace
        # - **clusterName**: cluster name
        # - **image**: image name
        # - **imageRepoName**: image repository name
        # - **imageRepoNamespace**: image repository namespace
        # - **imageRepoTag**: image tag
        # - **imageDigest**: image digest.
        self.container_field_name = container_field_name
        # The value that corresponds to **ContainerFieldName**.
        self.container_field_value = container_field_value
        # The page number of the first page to display in the query results. Default value: **1**, which indicates that the results start from page 1.
        self.current_page = current_page
        # The CVE ID.
        # > Call the [DescribeVulListPage](~~DescribeVulListPage~~) operation to obtain this parameter.
        self.cve_id = cve_id
        # Specifies whether the vulnerability is handled. Valid values:
        # 
        # - **y**: handled
        # - **n**: not handled.
        self.dealed = dealed
        # The ID of the asset group.
        self.group_id = group_id
        # The language type of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The priority of the vulnerability fix to query. Separate multiple priorities with commas (,). Valid values:
        # 
        # - **asap**: high
        # - **later**: medium
        # - **nntf**: low.
        self.necessity = necessity
        # The number of vulnerability entries per page in a paged query. Default value: 10, which indicates that 10 vulnerability entries are displayed per page.
        self.page_size = page_size
        # Specifies whether Runtime Application Self-Protection (RASP) supports real-time protection against the vulnerability. Valid values:
        # 
        # - **0**: Not supported.
        # - **1**: Supported.
        self.rasp_defend = rasp_defend
        # The ID of the Alibaba Cloud account that is added as one of the member accounts in a resource folder.
        # > Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The label used for filtering. Valid values:
        # 
        # - **Restart required**
        # - **Remote utilization**
        # - **EXP exists**
        # - **Available**
        # - **Privilege escalation**
        # - **Code execution**
        self.search_tags = search_tags
        # The container query type. Valid values:
        # 
        # - **containerId**: container ID
        # - **uuid**: asset ID.
        self.target_type = target_type
        # The type of the vulnerability to query. Default value: cve. Valid values:
        # 
        # - **cve**: Linux software vulnerability
        # - **sys**: Windows system vulnerability
        # - **cms**: Web-CMS vulnerability
        # - **app**: application vulnerability (network scan)
        # - **sca**: application vulnerability (software constituency parsing).
        self.type = type
        # The UUIDs of the servers to query. Separate multiple UUIDs with commas (,).
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

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.attach_types is not None:
            result['AttachTypes'] = self.attach_types

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.search_tags is not None:
            result['SearchTags'] = self.search_tags

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AttachTypes') is not None:
            self.attach_types = m.get('AttachTypes')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SearchTags') is not None:
            self.search_tags = m.get('SearchTags')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

