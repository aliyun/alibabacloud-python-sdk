# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportNodesStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        end_time: str = None,
        issue_category: str = None,
        nodes_shrink: str = None,
        reason: str = None,
        start_time: str = None,
    ):
        # The description.
        self.description = description
        # The end time of the node issue. The time is in the ISO 8601 format \\`yyyy-MM-ddTHH:mm:ss+0800\\` and includes the time zone.
        self.end_time = end_time
        # The category of the issue. This parameter is required when \\`Reason\\` is set to \\`HardwareError\\`. Valid values:<br>
        # ● hardware-cpu-error: CPU failure<br>
        # ● hardware-gpu-error: GPU failure<br>
        # ● hardware-motherboard-error: Motherboard failure<br>
        # ● hardware-mem-error: Memory failure<br>
        # ● hardware-power-error: Power supply failure<br>
        # ● hardware-disk-error: Disk failure
        # ● hardware-networkcard-error: Network interface card failure<br>
        # ● hardware-fan-error: Fan failure<br>
        # ● hardware-cable-error: Network cable failure<br>
        # ● others: Other<br><br><br><br><br><br><br><br><br>
        self.issue_category = issue_category
        # The list of nodes.
        self.nodes_shrink = nodes_shrink
        # The impact of the issue on the Lingjun node.
        # Valid values:
        # ● HardwareError: A hardware error occurred.
        # ● SoftwareError: A software error occurred.
        # ● NetworkError: A network error occurred.
        # ● Others: Other issues. If none of the preceding values apply, set this parameter to \\`Others\\` and provide details in the \\`Description\\` parameter.
        self.reason = reason
        # The start time of the node issue. The time is in the ISO 8601 format \\`yyyy-MM-ddTHH:mm:ss+0800\\` and includes the time zone.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.issue_category is not None:
            result['IssueCategory'] = self.issue_category

        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IssueCategory') is not None:
            self.issue_category = m.get('IssueCategory')

        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

