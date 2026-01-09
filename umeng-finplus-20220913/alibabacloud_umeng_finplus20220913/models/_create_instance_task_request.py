# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        calback_url: str = None,
        client_id: int = None,
        dataset_ids: str = None,
        monitor_type: str = None,
        name: str = None,
        output_config: str = None,
        request_id: str = None,
        score_strategy_config: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.calback_url = calback_url
        self.client_id = client_id
        # This parameter is required.
        self.dataset_ids = dataset_ids
        self.monitor_type = monitor_type
        # This parameter is required.
        self.name = name
        self.output_config = output_config
        self.request_id = request_id
        self.score_strategy_config = score_strategy_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.calback_url is not None:
            result['CalbackUrl'] = self.calback_url

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.name is not None:
            result['Name'] = self.name

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.score_strategy_config is not None:
            result['ScoreStrategyConfig'] = self.score_strategy_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CalbackUrl') is not None:
            self.calback_url = m.get('CalbackUrl')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScoreStrategyConfig') is not None:
            self.score_strategy_config = m.get('ScoreStrategyConfig')

        return self

