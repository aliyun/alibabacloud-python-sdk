# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class NewJobOrderRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        callback_url: str = None,
        change_type: str = None,
        client_system: str = None,
        client_unique_id: str = None,
        creator: str = None,
        params: Dict[str, Any] = None,
        refer_url: str = None,
        request_id: str = None,
        title: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.callback_url = callback_url
        # This parameter is required.
        self.change_type = change_type
        # This parameter is required.
        self.client_system = client_system
        # This parameter is required.
        self.client_unique_id = client_unique_id
        self.creator = creator
        # This parameter is required.
        self.params = params
        self.refer_url = refer_url
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.client_system is not None:
            result['ClientSystem'] = self.client_system

        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.params is not None:
            result['Params'] = self.params

        if self.refer_url is not None:
            result['ReferUrl'] = self.refer_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')

        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ReferUrl') is not None:
            self.refer_url = m.get('ReferUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

