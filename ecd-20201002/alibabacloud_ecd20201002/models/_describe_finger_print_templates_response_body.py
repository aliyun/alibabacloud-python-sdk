# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class DescribeFingerPrintTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        finger_print_templates: List[main_models.DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates] = None,
        request_id: str = None,
    ):
        # The fingerprint templates.
        self.finger_print_templates = finger_print_templates
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.finger_print_templates:
            for v1 in self.finger_print_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FingerPrintTemplates'] = []
        if self.finger_print_templates is not None:
            for k1 in self.finger_print_templates:
                result['FingerPrintTemplates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.finger_print_templates = []
        if m.get('FingerPrintTemplates') is not None:
            for k1 in m.get('FingerPrintTemplates'):
                temp_model = main_models.DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates()
                self.finger_print_templates.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        creation_time: str = None,
        description: str = None,
        end_user_id: str = None,
        index: int = None,
        login_time: str = None,
        office_site_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        self.client_id = client_id
        # The time when the template was created.
        self.creation_time = creation_time
        # The description of the template.
        self.description = description
        # The user ID.
        self.end_user_id = end_user_id
        # The index.
        self.index = index
        # The logon time.
        self.login_time = login_time
        # The office network ID.
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.index is not None:
            result['Index'] = self.index

        if self.login_time is not None:
            result['LoginTime'] = self.login_time

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        return self

