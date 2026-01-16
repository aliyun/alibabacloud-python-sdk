# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListShardRecoveriesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListShardRecoveriesResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListShardRecoveriesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListShardRecoveriesResponseBodyResult(DaraModel):
    def __init__(
        self,
        bytes_percent: str = None,
        bytes_total: int = None,
        files_percent: str = None,
        files_total: int = None,
        index: str = None,
        source_host: str = None,
        source_node: str = None,
        stage: str = None,
        target_host: str = None,
        target_node: str = None,
        translog_ops: int = None,
        translog_ops_percent: str = None,
    ):
        # The data restoration progress.
        self.bytes_percent = bytes_percent
        # The total amount of data that is restored.
        self.bytes_total = bytes_total
        # The file execution progress.
        self.files_percent = files_percent
        # The total number of files.
        self.files_total = files_total
        # The name of the index.
        self.index = index
        # The IP address of the source node.
        self.source_host = source_host
        # The name of the source node.
        self.source_node = source_node
        # The data restoration status. Valid values:
        # 
        # *   done: Data restoration is complete.
        # *   finalize: Data is being cleared.
        # *   index: Index metadata is being read, and bytes are being copied from source to destination.
        # *   init: Data restoration is not started.
        # *   start: Data restoration is started.
        # *   translog: Translogs are being redone.
        self.stage = stage
        # The IP address of the destination node.
        self.target_host = target_host
        # The name of the destination node.
        self.target_node = target_node
        # The number of translog operations to be restored.
        self.translog_ops = translog_ops
        # The restoration progress of translog operations.
        self.translog_ops_percent = translog_ops_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes_percent is not None:
            result['bytesPercent'] = self.bytes_percent

        if self.bytes_total is not None:
            result['bytesTotal'] = self.bytes_total

        if self.files_percent is not None:
            result['filesPercent'] = self.files_percent

        if self.files_total is not None:
            result['filesTotal'] = self.files_total

        if self.index is not None:
            result['index'] = self.index

        if self.source_host is not None:
            result['sourceHost'] = self.source_host

        if self.source_node is not None:
            result['sourceNode'] = self.source_node

        if self.stage is not None:
            result['stage'] = self.stage

        if self.target_host is not None:
            result['targetHost'] = self.target_host

        if self.target_node is not None:
            result['targetNode'] = self.target_node

        if self.translog_ops is not None:
            result['translogOps'] = self.translog_ops

        if self.translog_ops_percent is not None:
            result['translogOpsPercent'] = self.translog_ops_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bytesPercent') is not None:
            self.bytes_percent = m.get('bytesPercent')

        if m.get('bytesTotal') is not None:
            self.bytes_total = m.get('bytesTotal')

        if m.get('filesPercent') is not None:
            self.files_percent = m.get('filesPercent')

        if m.get('filesTotal') is not None:
            self.files_total = m.get('filesTotal')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('sourceHost') is not None:
            self.source_host = m.get('sourceHost')

        if m.get('sourceNode') is not None:
            self.source_node = m.get('sourceNode')

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        if m.get('targetHost') is not None:
            self.target_host = m.get('targetHost')

        if m.get('targetNode') is not None:
            self.target_node = m.get('targetNode')

        if m.get('translogOps') is not None:
            self.translog_ops = m.get('translogOps')

        if m.get('translogOpsPercent') is not None:
            self.translog_ops_percent = m.get('translogOpsPercent')

        return self

