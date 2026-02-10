# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperationSuspEventsRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        operation: str = None,
        source_ip: str = None,
        sub_operation: str = None,
        suspicious_event_ids: str = None,
        warn_type: str = None,
    ):
        # The ID of the request source.
        # 
        # Set the value to **sas**, which indicates that the request is sent from Security Center.
        self.from_ = from_
        # The operation that you want to perform on alerts. Valid values:
        # 
        # *   **deal**: quarantines the source file of the malicious process.
        # *   **ignore**: ignores the alerts.
        # *   **mark_mis_info**: marks the alerts as false positives by adding the alerts to the whitelist.
        # *   **rm_mark_mis_info**: cancels false positives by removing the alerts from the whitelist.
        # *   **offline_handled**: marks the alerts as handled.
        # 
        # This parameter is required.
        self.operation = operation
        # The source IP address of the request.
        self.source_ip = source_ip
        # The suboperation that you want to perform when you quarantine the source file of the malicious process. Valid values:
        # 
        # *   **killAndQuaraFileByPidAndMd5andPath**: terminates the process based on its process ID (PID) and quarantines the source file of the process.
        # *   **quaraFileByMd5andPath**: quarantines the source file of the process.
        # *   **killAndQuaraFileByMd5andPath**: terminates the process and quarantines the source file of the process.
        self.sub_operation = sub_operation
        # The IDs of alert events.
        # 
        # > You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to obtain the IDs of alert events from the SecurityEventIds response parameter.
        # 
        # This parameter is required.
        self.suspicious_event_ids = suspicious_event_ids
        # The type of the exceptions. Valid values:
        # 
        # *   **alarm**: alerts
        # *   **null**: exceptions
        self.warn_type = warn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.sub_operation is not None:
            result['SubOperation'] = self.sub_operation

        if self.suspicious_event_ids is not None:
            result['SuspiciousEventIds'] = self.suspicious_event_ids

        if self.warn_type is not None:
            result['WarnType'] = self.warn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SubOperation') is not None:
            self.sub_operation = m.get('SubOperation')

        if m.get('SuspiciousEventIds') is not None:
            self.suspicious_event_ids = m.get('SuspiciousEventIds')

        if m.get('WarnType') is not None:
            self.warn_type = m.get('WarnType')

        return self

