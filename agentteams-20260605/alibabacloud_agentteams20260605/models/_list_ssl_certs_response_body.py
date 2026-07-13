# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class ListSslCertsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListSslCertsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.items = items
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSslCertsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSslCertsResponseBodyItems(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        chain_completed: bool = None,
        common_name: str = None,
        domain: str = None,
        issuer: str = None,
        not_after_timestamp: int = None,
        not_before_timestamp: int = None,
    ):
        self.algorithm = algorithm
        self.cert_id = cert_id
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.chain_completed = chain_completed
        self.common_name = common_name
        self.domain = domain
        self.issuer = issuer
        self.not_after_timestamp = not_after_timestamp
        self.not_before_timestamp = not_before_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.chain_completed is not None:
            result['ChainCompleted'] = self.chain_completed

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.not_after_timestamp is not None:
            result['NotAfterTimestamp'] = self.not_after_timestamp

        if self.not_before_timestamp is not None:
            result['NotBeforeTimestamp'] = self.not_before_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('ChainCompleted') is not None:
            self.chain_completed = m.get('ChainCompleted')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('NotAfterTimestamp') is not None:
            self.not_after_timestamp = m.get('NotAfterTimestamp')

        if m.get('NotBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('NotBeforeTimestamp')

        return self

