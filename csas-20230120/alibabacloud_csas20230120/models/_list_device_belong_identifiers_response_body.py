# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDeviceBelongIdentifiersResponseBody(DaraModel):
    def __init__(
        self,
        identifiers: List[main_models.ListDeviceBelongIdentifiersResponseBodyIdentifiers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The device ownership identifier records on the current page. An empty list is returned if no matching records are found.
        self.identifiers = identifiers
        # A reserved pagination field. No valid value is returned in the current version.
        self.max_results = max_results
        # A reserved pagination cursor. No valid value is returned in the current version.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records that match the filter conditions for the current tenant.
        self.total_count = total_count

    def validate(self):
        if self.identifiers:
            for v1 in self.identifiers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Identifiers'] = []
        if self.identifiers is not None:
            for k1 in self.identifiers:
                result['Identifiers'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.identifiers = []
        if m.get('Identifiers') is not None:
            for k1 in m.get('Identifiers'):
                temp_model = main_models.ListDeviceBelongIdentifiersResponseBodyIdentifiers()
                self.identifiers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDeviceBelongIdentifiersResponseBodyIdentifiers(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        identifier_id: str = None,
        identifier_type: str = None,
        identifier_value: str = None,
    ):
        # The time when the record was created. The time is in RFC 3339 format and includes time zone information.
        self.create_time = create_time
        # The ID of the identifier record, returned as a decimal string. You can use the ID to query or remove the record.
        self.identifier_id = identifier_id
        # The identifier type. MAC indicates the MAC address of the network interface controller (NIC), SystemSN indicates the system serial number, and BIOSSN indicates the BIOS serial number.
        self.identifier_type = identifier_type
        # The identifier value in the record. MAC addresses are in the lowercase colon-separated format. System serial numbers and BIOS serial numbers are returned as recorded.
        self.identifier_value = identifier_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.identifier_id is not None:
            result['IdentifierId'] = self.identifier_id

        if self.identifier_type is not None:
            result['IdentifierType'] = self.identifier_type

        if self.identifier_value is not None:
            result['IdentifierValue'] = self.identifier_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IdentifierId') is not None:
            self.identifier_id = m.get('IdentifierId')

        if m.get('IdentifierType') is not None:
            self.identifier_type = m.get('IdentifierType')

        if m.get('IdentifierValue') is not None:
            self.identifier_value = m.get('IdentifierValue')

        return self

