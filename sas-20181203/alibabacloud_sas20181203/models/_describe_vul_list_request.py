# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulListRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        attach_types: str = None,
        cluster_id: str = None,
        current_page: int = None,
        dealed: str = None,
        group_id: str = None,
        ids: str = None,
        lang: str = None,
        name: str = None,
        necessity: str = None,
        next_token: str = None,
        page_size: int = None,
        rasp_defend: int = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        status_list: str = None,
        target_type: str = None,
        type: str = None,
        use_next_token: bool = None,
        uuids: str = None,
        vpc_instance_ids: str = None,
    ):
        # The name of the vulnerability.
        self.alias_name = alias_name
        # The additional type of the vulnerabilities. You need to specify this parameter when you query application vulnerabilities. Set the value to **sca**. If you set **Type** to **app**, you must specify this parameter.
        # 
        # > If you set this parameter to **sca**, application vulnerabilities and the vulnerabilities that are detected based on software component analysis are queried. If you do not specify this parameter, only application vulnerabilities are queried.
        self.attach_types = attach_types
        # The cluster ID.
        self.cluster_id = cluster_id
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether the vulnerabilities are fixed. Valid values:
        # 
        # *   **y**: yes
        # *   **n**: no
        self.dealed = dealed
        # The ID of the asset group.
        # 
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of asset groups.
        self.group_id = group_id
        # The IDs of vulnerabilities. You can specify up to 50 IDs. Separate multiple IDs with commas (,).
        self.ids = ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The alias of the vulnerability.
        self.name = name
        # The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values:
        # 
        # *   **asap**: high
        # *   **later**: medium
        # *   **nntf**: low
        self.necessity = necessity
        # The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # Indicates whether the application protection feature is supported. Valid values:
        # 
        # - **0**: no.
        # 
        # - **1**: yes.
        self.rasp_defend = rasp_defend
        # The remarks for the asset affected by the vulnerability. The value can be the private IP address, public IP address, or name of the asset.
        self.remark = remark
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The status of the vulnerability. Separate multiple statuses with commas (,). Valid values:
        # 
        # - 1: unfixed
        # - 2: fix failed
        # - 3: rollback failed
        # - 4: being fixed
        # - 5: being rolled back
        # - 6: being verified
        # - 7: fixed
        # - 8: fixed and to be restarted
        # - 9: rolled back
        # - 10: ignored
        # - 11: rolled back and to be restarted
        # - 12: not found
        # - 20: expired
        self.status_list = status_list
        # The type of the asset on which the vulnerability is detected. Valid values:
        # 
        # *   **k8s**: Kubernetes component.
        # *   **uuid**: server.
        # *   **containerId**: container.
        self.target_type = target_type
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability.
        # *   **app**: application vulnerability that is detected by using web scanner
        # *   **emg**: urgent vulnerability.
        # *   **sca**: application vulnerability that is detected by using software component analysis
        # 
        # This parameter is required.
        self.type = type
        # Specifies whether to use NextToken to query the data of vulnerabilities. If you set UseNextToken to true, the value of TotalCount is not returned. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.use_next_token = use_next_token
        # The UUIDs of the servers on which you want to query the vulnerabilities. Separate multiple UUIDs with commas (,).
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the UUIDs.
        self.uuids = uuids
        # The ID of the virtual private cloud (VPC) in which the vulnerabilities are detected. Separate multiple IDs with commas (,).
        self.vpc_instance_ids = vpc_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.attach_types is not None:
            result['AttachTypes'] = self.attach_types

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.vpc_instance_ids is not None:
            result['VpcInstanceIds'] = self.vpc_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AttachTypes') is not None:
            self.attach_types = m.get('AttachTypes')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('VpcInstanceIds') is not None:
            self.vpc_instance_ids = m.get('VpcInstanceIds')

        return self

