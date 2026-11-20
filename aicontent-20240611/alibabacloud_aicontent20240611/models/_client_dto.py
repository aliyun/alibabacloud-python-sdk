# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClientDTO(DaraModel):
    def __init__(
        self,
        address: str = None,
        allowed_model_group_config: str = None,
        allowed_models: str = None,
        client_uuid: str = None,
        contact: str = None,
        delete_tag: int = None,
        discount: float = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        level: int = None,
        main: int = None,
        name: str = None,
        node_type: str = None,
        parent_id: int = None,
        remark: str = None,
        user_id: int = None,
    ):
        # The company address.
        self.address = address
        # The authorization management configuration in the format of {"model_ids":[...],"group_ids":[...]}. An empty value indicates that group authorization is not used.
        self.allowed_model_group_config = allowed_model_group_config
        # The list of allowed model IDs, separated by commas. An empty value indicates all models.
        self.allowed_models = allowed_models
        # The customer UUID.
        self.client_uuid = client_uuid
        # The contact information.
        self.contact = contact
        # The status. A value of 0 indicates enabled, and a non-zero value indicates disabled.
        self.delete_tag = delete_tag
        # The discount factor. A value of 1.0 indicates no discount.
        self.discount = discount
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # ID
        self.id = id
        # The hierarchy level. Valid values: 1 to 5.
        self.level = level
        # The account type. A value of 0 indicates a main account, and a value of 1 indicates a regular account.
        self.main = main
        # The customer name.
        self.name = name
        # The node type. Valid values: department: Department. user: User node, which is a leaf in the department tree.
        self.node_type = node_type
        # The parent department ID. An empty value indicates the top level.
        self.parent_id = parent_id
        # The remarks.
        self.remark = remark
        # The user ID. This field has a value only when the node type is user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.allowed_model_group_config is not None:
            result['allowedModelGroupConfig'] = self.allowed_model_group_config

        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.client_uuid is not None:
            result['clientUuid'] = self.client_uuid

        if self.contact is not None:
            result['contact'] = self.contact

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.discount is not None:
            result['discount'] = self.discount

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.level is not None:
            result['level'] = self.level

        if self.main is not None:
            result['main'] = self.main

        if self.name is not None:
            result['name'] = self.name

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.remark is not None:
            result['remark'] = self.remark

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('allowedModelGroupConfig') is not None:
            self.allowed_model_group_config = m.get('allowedModelGroupConfig')

        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('clientUuid') is not None:
            self.client_uuid = m.get('clientUuid')

        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('main') is not None:
            self.main = m.get('main')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

