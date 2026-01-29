# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RelieveAccountRelationRequest(DaraModel):
    def __init__(
        self,
        child_user_id: int = None,
        parent_user_id: int = None,
        relation_id: int = None,
        relation_type: str = None,
        request_id: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used as the member. You must set the RelationId parameter or all of the ParentUserId, ChildUserId, and RelationType parameters.
        self.child_user_id = child_user_id
        # The ID of the Alibaba Cloud account that is used as the management account. You must set the RelationId parameter or all of the ParentUserId, ChildUserId, and RelationType parameters.
        self.parent_user_id = parent_user_id
        # The ID of the financial relationship between the management account and the member. You must set the RelationId parameter or all of the ParentUserId, ChildUserId, and RelationType parameters.
        self.relation_id = relation_id
        # The type of the financial relationship. Set the value to enterprise_group.
        self.relation_type = relation_type
        # The unique ID of the request. The ID is used to mark a request and troubleshoot a problem.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_user_id is not None:
            result['ChildUserId'] = self.child_user_id

        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildUserId') is not None:
            self.child_user_id = m.get('ChildUserId')

        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

