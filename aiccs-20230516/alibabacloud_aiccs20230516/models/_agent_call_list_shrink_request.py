# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentCallListShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_tag: str = None,
        call_date: str = None,
        end_call_date: str = None,
        number_md5s_shrink: str = None,
        numbers_shrink: str = None,
        owner_id: int = None,
        page: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags_shrink: str = None,
    ):
        # 坐席ID
        self.agent_id = agent_id
        # 坐席标签
        self.agent_tag = agent_tag
        # 开始外呼时间
        # 
        # This parameter is required.
        self.call_date = call_date
        # 结束外呼时间
        # 
        # This parameter is required.
        self.end_call_date = end_call_date
        # 号码MD5列表
        self.number_md5s_shrink = number_md5s_shrink
        # 号码列表
        self.numbers_shrink = numbers_shrink
        self.owner_id = owner_id
        # 页数
        # 
        # This parameter is required.
        self.page = page
        # 每页外呼记录数
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 用户自定义标签列表
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag

        if self.call_date is not None:
            result['CallDate'] = self.call_date

        if self.end_call_date is not None:
            result['EndCallDate'] = self.end_call_date

        if self.number_md5s_shrink is not None:
            result['NumberMD5s'] = self.number_md5s_shrink

        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')

        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')

        if m.get('EndCallDate') is not None:
            self.end_call_date = m.get('EndCallDate')

        if m.get('NumberMD5s') is not None:
            self.number_md5s_shrink = m.get('NumberMD5s')

        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

