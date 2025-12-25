# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListExchangesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListExchangesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListExchangesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListExchangesResponseBodyData(DaraModel):
    def __init__(
        self,
        exchanges: List[main_models.ListExchangesResponseBodyDataExchanges] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The exchanges.
        self.exchanges = exchanges
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token that marks the end of the current returned page.``
        # 
        # *   If the value of this parameter is empty, the next query is not required and the token used to start the next query is unavailable.``
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.``
        self.next_token = next_token

    def validate(self):
        if self.exchanges:
            for v1 in self.exchanges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Exchanges'] = []
        if self.exchanges is not None:
            for k1 in self.exchanges:
                result['Exchanges'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchanges = []
        if m.get('Exchanges') is not None:
            for k1 in m.get('Exchanges'):
                temp_model = main_models.ListExchangesResponseBodyDataExchanges()
                self.exchanges.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListExchangesResponseBodyDataExchanges(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        auto_delete_state: bool = None,
        create_time: int = None,
        exchange_type: str = None,
        internal: bool = None,
        name: str = None,
        vhost_name: str = None,
    ):
        # The attributes. This parameter is unavailable in the current version.
        self.attributes = attributes
        # Indicates whether the exchange was automatically deleted.
        self.auto_delete_state = auto_delete_state
        # The timestamp that indicates when the exchange was created. Unit: milliseconds.
        self.create_time = create_time
        # The exchange type.
        self.exchange_type = exchange_type
        self.internal = internal
        # The exchange name.
        self.name = name
        # The vhost name.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type

        if self.internal is not None:
            result['Internal'] = self.internal

        if self.name is not None:
            result['Name'] = self.name

        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')

        if m.get('Internal') is not None:
            self.internal = m.get('Internal')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')

        return self

