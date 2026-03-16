# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupsRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        business_channel: str = None,
        exclude_attached_login_policy_groups: bool = None,
        group_id: str = None,
        group_name: str = None,
        idp_id: str = None,
        login_policy_id: str = None,
        page_number: int = None,
        page_size: int = None,
        solution_id: str = None,
        transfer_file_need_approval: bool = None,
    ):
        # > This parameter is not publicly available.
        self.biz_type = biz_type
        self.business_channel = business_channel
        # 是否排除已关联登录策略的用户组。
        self.exclude_attached_login_policy_groups = exclude_attached_login_policy_groups
        # The ID of the user group.
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name
        self.idp_id = idp_id
        # 指定关联的登录策略筛选。
        self.login_policy_id = login_policy_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # > This parameter is not publicly available.
        self.solution_id = solution_id
        # Indicates whether the file approval feature is enabled.
        self.transfer_file_need_approval = transfer_file_need_approval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.exclude_attached_login_policy_groups is not None:
            result['ExcludeAttachedLoginPolicyGroups'] = self.exclude_attached_login_policy_groups

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.login_policy_id is not None:
            result['LoginPolicyId'] = self.login_policy_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        if self.transfer_file_need_approval is not None:
            result['TransferFileNeedApproval'] = self.transfer_file_need_approval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('ExcludeAttachedLoginPolicyGroups') is not None:
            self.exclude_attached_login_policy_groups = m.get('ExcludeAttachedLoginPolicyGroups')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('LoginPolicyId') is not None:
            self.login_policy_id = m.get('LoginPolicyId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        if m.get('TransferFileNeedApproval') is not None:
            self.transfer_file_need_approval = m.get('TransferFileNeedApproval')

        return self

