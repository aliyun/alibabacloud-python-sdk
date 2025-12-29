# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceVpcRequest(DaraModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
        vpc_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        # vpc-2ze0i263cnn311nvj\\*\\*\\*\\*
        self.namespace_id = namespace_id
        # The ID of the request.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

