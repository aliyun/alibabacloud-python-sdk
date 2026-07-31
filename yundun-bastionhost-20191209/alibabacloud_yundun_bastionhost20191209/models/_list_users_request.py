# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        instance_id: str = None,
        mobile: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
        source_user_id: str = None,
        user_group_id: str = None,
        user_name: str = None,
        user_state: str = None,
    ):
        # The display name of the user that you want to query. Only exact match is supported.
        self.display_name = display_name
        # The instance ID of the bastion host for which you want to query the user list.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The mobile phone number of the user that you want to query. Only exact match is supported.
        self.mobile = mobile
        # The page number of the current page in a paging query. Default value: **1**.
        self.page_number = page_number
        # The maximum number of entries per page in a paging query.  
        # The maximum value of the PageSize parameter is 100. The default number of entries per page is 20. If PageSize is left empty, 20 entries are returned by default.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The region ID of the bastion host for which you want to query the user list.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The source of the user that you want to query. Valid values:
        # - **Local**: local user
        # - **Ram**: Resource Access Management (RAM) user
        # - **AD**: AD user
        # - **LDAP**: LDAP user
        self.source = source
        # The unique identity of the user that you want to query. Only exact match is supported.
        # > This parameter is the unique identity of the Resource Access Management (RAM) user that corresponds to the bastion host user. This parameter takes effect when the source of the newly created user is a RAM user (that is, **Source** is set to **Ram**). You can invoke the [ListUsers](https://help.aliyun.com/document_detail/28684.html) operation of access control and obtain this parameter from the **UserId** field in the response.
        self.source_user_id = source_user_id
        # The ID of the user group that you want to query.
        # > You can call the [ListUserGroups](https://help.aliyun.com/document_detail/204509.html) operation to obtain this parameter.
        self.user_group_id = user_group_id
        # The logon name of the user that you want to query. Only exact match is supported.
        self.user_name = user_name
        # The status of the user that you want to query. Valid values:
        # - **Normal**: normal
        # - **Frozen**: locked
        # - **Expired**: expired
        # - **RemoteDeleted**: user source deleted
        # - **Inactive**: inactive due to prolonged absence of logon
        # - **PasswordExpired**: password expired
        # - **RemoteDNChanged**: user DN updated
        # - **RemoteFrozen**: frozen on the RAM side
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_state is not None:
            result['UserState'] = self.user_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')

        return self

