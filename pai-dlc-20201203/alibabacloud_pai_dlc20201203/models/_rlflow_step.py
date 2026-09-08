# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowStep(DaraModel):
    def __init__(
        self,
        buffer_wait_p50: float = None,
        gap_sec: float = None,
        idle_sec: float = None,
        nsamples: int = None,
        ntrajs: int = None,
        prod_end_ms: int = None,
        prod_start_ms: int = None,
        rollout_p50: float = None,
        rollout_sec: float = None,
        step: int = None,
        tfwd_start_ms: int = None,
        topt_end_ms: int = None,
        trollout_end_ms: int = None,
        trollout_start_ms: int = None,
        ttrain_end_ms: int = None,
        ttrain_start_ms: int = None,
        tupdate_ms: int = None,
        train_sec: float = None,
    ):
        # The P50 latency in seconds from when trajectories of the step enter the buffer to when batching occurs.
        self.buffer_wait_p50 = buffer_wait_p50
        # The gap duration in seconds, calculated as train started − rollout finished. This represents batching or transfer wait time.
        self.gap_sec = gap_sec
        # The training idle time in seconds, calculated as the current step training start − the previous step training end. If no marker is present, the value falls back to the current step forward computation start − the previous step optimizer end. A value greater than 0 indicates that the trainer is waiting for data.
        self.idle_sec = idle_sec
        # The number of samples (UIDs) consumed by the step.
        self.nsamples = nsamples
        # The number of trajectories executed in the step.
        self.ntrajs = ntrajs
        # The latest time when trajectories of the step enter the buffer, in milliseconds.
        self.prod_end_ms = prod_end_ms
        # The earliest time when trajectories of the step enter the buffer, in milliseconds.
        self.prod_start_ms = prod_start_ms
        # The P50 latency in seconds from when trajectories of the step start execution to when they enter the buffer.
        self.rollout_p50 = rollout_p50
        # The rollout duration in seconds, calculated as rollout finished − rollout started. This value is null if no marker is present.
        self.rollout_sec = rollout_sec
        # The global step ordinal number.
        self.step = step
        # The forward computation start time, in milliseconds.
        self.tfwd_start_ms = tfwd_start_ms
        # The optimizer end time, in milliseconds.
        self.topt_end_ms = topt_end_ms
        # The node operation log "Step N rollout finished" time, in milliseconds.
        self.trollout_end_ms = trollout_end_ms
        # The node operation log "Step N rollout started" time, in milliseconds (taken from agent_collect_time).
        self.trollout_start_ms = trollout_start_ms
        # The node operation log "Step N train finished" time, in milliseconds.
        self.ttrain_end_ms = ttrain_end_ms
        # The node operation log "Step N train started" time, in milliseconds.
        self.ttrain_start_ms = ttrain_start_ms
        # The TRAIN_UPDATE (parameter update) time, in milliseconds.
        self.tupdate_ms = tupdate_ms
        # The training duration in seconds. This value is preferentially calculated as train finished − train started. If no marker is present, the value falls back to the duration from batching to training completion. This value is null if global_step is duplicated because of a job restart.
        self.train_sec = train_sec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buffer_wait_p50 is not None:
            result['BufferWaitP50'] = self.buffer_wait_p50

        if self.gap_sec is not None:
            result['GapSec'] = self.gap_sec

        if self.idle_sec is not None:
            result['IdleSec'] = self.idle_sec

        if self.nsamples is not None:
            result['NSamples'] = self.nsamples

        if self.ntrajs is not None:
            result['NTrajs'] = self.ntrajs

        if self.prod_end_ms is not None:
            result['ProdEndMs'] = self.prod_end_ms

        if self.prod_start_ms is not None:
            result['ProdStartMs'] = self.prod_start_ms

        if self.rollout_p50 is not None:
            result['RolloutP50'] = self.rollout_p50

        if self.rollout_sec is not None:
            result['RolloutSec'] = self.rollout_sec

        if self.step is not None:
            result['Step'] = self.step

        if self.tfwd_start_ms is not None:
            result['TFwdStartMs'] = self.tfwd_start_ms

        if self.topt_end_ms is not None:
            result['TOptEndMs'] = self.topt_end_ms

        if self.trollout_end_ms is not None:
            result['TRolloutEndMs'] = self.trollout_end_ms

        if self.trollout_start_ms is not None:
            result['TRolloutStartMs'] = self.trollout_start_ms

        if self.ttrain_end_ms is not None:
            result['TTrainEndMs'] = self.ttrain_end_ms

        if self.ttrain_start_ms is not None:
            result['TTrainStartMs'] = self.ttrain_start_ms

        if self.tupdate_ms is not None:
            result['TUpdateMs'] = self.tupdate_ms

        if self.train_sec is not None:
            result['TrainSec'] = self.train_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BufferWaitP50') is not None:
            self.buffer_wait_p50 = m.get('BufferWaitP50')

        if m.get('GapSec') is not None:
            self.gap_sec = m.get('GapSec')

        if m.get('IdleSec') is not None:
            self.idle_sec = m.get('IdleSec')

        if m.get('NSamples') is not None:
            self.nsamples = m.get('NSamples')

        if m.get('NTrajs') is not None:
            self.ntrajs = m.get('NTrajs')

        if m.get('ProdEndMs') is not None:
            self.prod_end_ms = m.get('ProdEndMs')

        if m.get('ProdStartMs') is not None:
            self.prod_start_ms = m.get('ProdStartMs')

        if m.get('RolloutP50') is not None:
            self.rollout_p50 = m.get('RolloutP50')

        if m.get('RolloutSec') is not None:
            self.rollout_sec = m.get('RolloutSec')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('TFwdStartMs') is not None:
            self.tfwd_start_ms = m.get('TFwdStartMs')

        if m.get('TOptEndMs') is not None:
            self.topt_end_ms = m.get('TOptEndMs')

        if m.get('TRolloutEndMs') is not None:
            self.trollout_end_ms = m.get('TRolloutEndMs')

        if m.get('TRolloutStartMs') is not None:
            self.trollout_start_ms = m.get('TRolloutStartMs')

        if m.get('TTrainEndMs') is not None:
            self.ttrain_end_ms = m.get('TTrainEndMs')

        if m.get('TTrainStartMs') is not None:
            self.ttrain_start_ms = m.get('TTrainStartMs')

        if m.get('TUpdateMs') is not None:
            self.tupdate_ms = m.get('TUpdateMs')

        if m.get('TrainSec') is not None:
            self.train_sec = m.get('TrainSec')

        return self

