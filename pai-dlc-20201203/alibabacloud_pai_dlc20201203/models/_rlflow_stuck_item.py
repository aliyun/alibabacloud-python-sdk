# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowStuckItem(DaraModel):
    def __init__(
        self,
        idle_sec: int = None,
        last_ts_ms: int = None,
        milestone: str = None,
        nturns: int = None,
        prompt_uid: str = None,
        sample_index: str = None,
    ):
        # The number of idle seconds since NowMs. This value is the descending sort key of the Stuck list.
        self.idle_sec = idle_sec
        # The UNIX timestamp of the last event, in milliseconds.
        self.last_ts_ms = last_ts_ms
        # The current milestone where the entry is staying. Valid values:
        # - 已生成未下发: Generated but not delivered.
        # - 已下发未启动: Delivered but not started.
        # - 已启动待生成: Started and pending generation.
        # - 生成中: Generating.
        # - Rollout完成待打分: Rollout completed and pending scoring.
        # - 已打分待采样: Scored and pending sampling.
        # - 已采样待训练: Sampled and pending training.
        self.milestone = milestone
        # The number of completed generation rounds.
        self.nturns = nturns
        # The UID of the sample.
        self.prompt_uid = prompt_uid
        # The ordinal number of the trajectory.
        self.sample_index = sample_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idle_sec is not None:
            result['IdleSec'] = self.idle_sec

        if self.last_ts_ms is not None:
            result['LastTsMs'] = self.last_ts_ms

        if self.milestone is not None:
            result['Milestone'] = self.milestone

        if self.nturns is not None:
            result['NTurns'] = self.nturns

        if self.prompt_uid is not None:
            result['PromptUid'] = self.prompt_uid

        if self.sample_index is not None:
            result['SampleIndex'] = self.sample_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdleSec') is not None:
            self.idle_sec = m.get('IdleSec')

        if m.get('LastTsMs') is not None:
            self.last_ts_ms = m.get('LastTsMs')

        if m.get('Milestone') is not None:
            self.milestone = m.get('Milestone')

        if m.get('NTurns') is not None:
            self.nturns = m.get('NTurns')

        if m.get('PromptUid') is not None:
            self.prompt_uid = m.get('PromptUid')

        if m.get('SampleIndex') is not None:
            self.sample_index = m.get('SampleIndex')

        return self

