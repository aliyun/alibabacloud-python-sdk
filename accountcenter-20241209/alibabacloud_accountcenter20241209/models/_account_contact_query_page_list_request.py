# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccountContactQueryPageListRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page_no: int = None,
        page_size: int = None,
        private_contact: bool = None,
        query: str = None,
        shared_contact: bool = None,
        show_complete_info: bool = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page_no = page_no
        self.page_size = page_size
        self.private_contact = private_contact
        self.query = query
        self.shared_contact = shared_contact
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_contact is not None:
            result['PrivateContact'] = self.private_contact

        if self.query is not None:
            result['Query'] = self.query

        if self.shared_contact is not None:
            result['SharedContact'] = self.shared_contact

        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateContact') is not None:
            self.private_contact = m.get('PrivateContact')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SharedContact') is not None:
            self.shared_contact = m.get('SharedContact')

        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')

        return self

