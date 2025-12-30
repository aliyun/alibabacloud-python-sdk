# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobLogRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_id: str = None,
        log_type: str = None,
        offset: str = None,
        size: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The log type. Valid values:
        # 
        # *   stdout: standard output logs.
        # *   stderr: error output logs.
        # *   all: all logs.
        # 
        # Default value: all.
        self.log_type = log_type
        # The position where logs start to be read.
        # 
        # Unit: bytes.
        # 
        # Default value: 0.
        self.offset = offset
        # The maximum size of logs that you can read in a single request.
        # 
        # Unit: bytes.
        # 
        # Default value: 10240.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

