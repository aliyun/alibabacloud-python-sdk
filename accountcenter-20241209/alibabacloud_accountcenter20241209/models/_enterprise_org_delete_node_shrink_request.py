# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseOrgDeleteNodeShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        biz_name: str = None,
        ext_shrink: str = None,
        is_open_api: bool = None,
        node_id: str = None,
        node_type: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        show_complete_info: bool = None,
        tree_id: int = None,
    ):
        self.app_name = app_name
        self.biz_name = biz_name
        self.ext_shrink = ext_shrink
        self.is_open_api = is_open_api
        self.node_id = node_id
        self.node_type = node_type
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.show_complete_info = show_complete_info
        self.tree_id = tree_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.ext_shrink is not None:
            result['Ext'] = self.ext_shrink

        if self.is_open_api is not None:
            result['IsOpenApi'] = self.is_open_api

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info

        if self.tree_id is not None:
            result['TreeId'] = self.tree_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Ext') is not None:
            self.ext_shrink = m.get('Ext')

        if m.get('IsOpenApi') is not None:
            self.is_open_api = m.get('IsOpenApi')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')

        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')

        return self

