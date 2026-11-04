# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class UpdateContextStoreResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateContextStoreResponseBodyConfig = None,
        request_id: str = None,
        strategy_version: int = None,
    ):
        # The configuration properties after the runtime recall switch is updated. This block is not returned for other library update operations.
        self.config = config
        # The request ID, which is used to locate this request during troubleshooting.
        self.request_id = request_id
        # The strategy version number that takes effect after the update for the memory type. If the strategy remains unchanged, the version number is the same as before the update.
        self.strategy_version = strategy_version

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.strategy_version is not None:
            result['strategyVersion'] = self.strategy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.UpdateContextStoreResponseBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('strategyVersion') is not None:
            self.strategy_version = m.get('strategyVersion')

        return self

class UpdateContextStoreResponseBodyConfig(DaraModel):
    def __init__(
        self,
        runtime_recall_enabled: bool = None,
        runtime_recall_revision: int = None,
    ):
        # Indicates whether runtime recall is allowed after the experience library is updated.
        self.runtime_recall_enabled = runtime_recall_enabled
        # The runtime recall property version that takes effect after this update.
        self.runtime_recall_revision = runtime_recall_revision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.runtime_recall_enabled is not None:
            result['runtimeRecallEnabled'] = self.runtime_recall_enabled

        if self.runtime_recall_revision is not None:
            result['runtimeRecallRevision'] = self.runtime_recall_revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runtimeRecallEnabled') is not None:
            self.runtime_recall_enabled = m.get('runtimeRecallEnabled')

        if m.get('runtimeRecallRevision') is not None:
            self.runtime_recall_revision = m.get('runtimeRecallRevision')

        return self

