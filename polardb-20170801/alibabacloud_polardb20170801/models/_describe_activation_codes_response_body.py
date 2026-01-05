# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeActivationCodesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeActivationCodesResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried activation codes.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeActivationCodesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeActivationCodesResponseBodyItems(DaraModel):
    def __init__(
        self,
        activate_at: str = None,
        description: str = None,
        expire_at: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        mac_address: str = None,
        name: str = None,
        system_identifier: str = None,
    ):
        # The time when the activation code takes effect.
        self.activate_at = activate_at
        # The description of the activation code.
        self.description = description
        # The time when the activation code expires.
        self.expire_at = expire_at
        # The time when the activation code was generated.
        self.gmt_created = gmt_created
        # The time when the activation code was updated.
        self.gmt_modified = gmt_modified
        # The activation code ID.
        self.id = id
        # The media access control (MAC) address used in the generation of the activation code.
        self.mac_address = mac_address
        # The name of the activation code.
        self.name = name
        # The unique identifier of the database.
        self.system_identifier = system_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_at is not None:
            result['ActivateAt'] = self.activate_at

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.name is not None:
            result['Name'] = self.name

        if self.system_identifier is not None:
            result['SystemIdentifier'] = self.system_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateAt') is not None:
            self.activate_at = m.get('ActivateAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SystemIdentifier') is not None:
            self.system_identifier = m.get('SystemIdentifier')

        return self

