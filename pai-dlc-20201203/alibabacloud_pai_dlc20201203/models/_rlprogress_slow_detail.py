# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressSlowDetail(DaraModel):
    def __init__(
        self,
        elapsed: float = None,
        ip: str = None,
        ipc: str = None,
        is_pause: str = None,
        message: str = None,
        out_queue: str = None,
        pod: str = None,
        rank: int = None,
        rid: str = None,
        state_present: str = None,
        time: int = None,
        tokenizer_pid: str = None,
        worker_pid: int = None,
    ):
        # The elapsed time of the request, in seconds.
        self.elapsed = elapsed
        # worker IP
        self.ip = ip
        # The IPC channel identifier, which corresponds to the ipc field in the log.
        self.ipc = ipc
        # Indicates whether the request is paused. This is the raw value of the is_pause field in the log.
        self.is_pause = is_pause
        # The log message, truncated to 700 characters.
        self.message = message
        # The output queue length. This is the raw value of the out_queue field in the log.
        self.out_queue = out_queue
        # The name of the pod.
        self.pod = pod
        # The training rank.
        self.rank = rank
        # The inference request ID, which corresponds to the rid field in the log.
        self.rid = rid
        # Indicates whether the state is present. This is the raw value of the state_present field in the log.
        self.state_present = state_present
        # The log time, in UNIX seconds.
        self.time = time
        # The tokenizer process ID, which corresponds to the pid field in the log.
        self.tokenizer_pid = tokenizer_pid
        # The worker process ID.
        self.worker_pid = worker_pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elapsed is not None:
            result['Elapsed'] = self.elapsed

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ipc is not None:
            result['Ipc'] = self.ipc

        if self.is_pause is not None:
            result['IsPause'] = self.is_pause

        if self.message is not None:
            result['Message'] = self.message

        if self.out_queue is not None:
            result['OutQueue'] = self.out_queue

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.rank is not None:
            result['Rank'] = self.rank

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.state_present is not None:
            result['StatePresent'] = self.state_present

        if self.time is not None:
            result['Time'] = self.time

        if self.tokenizer_pid is not None:
            result['TokenizerPid'] = self.tokenizer_pid

        if self.worker_pid is not None:
            result['WorkerPid'] = self.worker_pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Elapsed') is not None:
            self.elapsed = m.get('Elapsed')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Ipc') is not None:
            self.ipc = m.get('Ipc')

        if m.get('IsPause') is not None:
            self.is_pause = m.get('IsPause')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OutQueue') is not None:
            self.out_queue = m.get('OutQueue')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('Rank') is not None:
            self.rank = m.get('Rank')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('StatePresent') is not None:
            self.state_present = m.get('StatePresent')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TokenizerPid') is not None:
            self.tokenizer_pid = m.get('TokenizerPid')

        if m.get('WorkerPid') is not None:
            self.worker_pid = m.get('WorkerPid')

        return self

