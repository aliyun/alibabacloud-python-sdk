# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UserStatistic(DaraModel):
    def __init__(
        self,
        accepted_mark_items_count: float = None,
        check_count: float = None,
        checked_accepted_count: float = None,
        checked_accuracy: float = None,
        mark_efficiency: float = None,
        mark_time: float = None,
        sampling_accuracy: float = None,
        sampling_count: float = None,
        sampling_error_count: float = None,
        total_mark_items_count: float = None,
        user_id: str = None,
    ):
        # Quantity of Data items passed
        self.accepted_mark_items_count = accepted_mark_items_count
        # Total inspection count
        self.check_count = check_count
        # Quantity passed in inspection
        self.checked_accepted_count = checked_accepted_count
        # Inspection accuracy.  
        # Inspection accuracy = Number Of Error inspected / Quantity inspected
        self.checked_accuracy = checked_accuracy
        # Annotation efficiency. Unit: items/hour  
        # Annotation efficiency = Quantity annotated / Annotation duration (including rejections)
        self.mark_efficiency = mark_efficiency
        # Annotation duration. Unit: hours
        self.mark_time = mark_time
        # Sampling accuracy.  
        # Validated accuracy = Number Of Error validated / Quantity validated
        self.sampling_accuracy = sampling_accuracy
        # Total sampling quantity
        self.sampling_count = sampling_count
        # Number Of Error in sampling
        self.sampling_error_count = sampling_error_count
        # Total Data items
        self.total_mark_items_count = total_mark_items_count
        # User ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted_mark_items_count is not None:
            result['AcceptedMarkItemsCount'] = self.accepted_mark_items_count

        if self.check_count is not None:
            result['CheckCount'] = self.check_count

        if self.checked_accepted_count is not None:
            result['CheckedAcceptedCount'] = self.checked_accepted_count

        if self.checked_accuracy is not None:
            result['CheckedAccuracy'] = self.checked_accuracy

        if self.mark_efficiency is not None:
            result['MarkEfficiency'] = self.mark_efficiency

        if self.mark_time is not None:
            result['MarkTime'] = self.mark_time

        if self.sampling_accuracy is not None:
            result['SamplingAccuracy'] = self.sampling_accuracy

        if self.sampling_count is not None:
            result['SamplingCount'] = self.sampling_count

        if self.sampling_error_count is not None:
            result['SamplingErrorCount'] = self.sampling_error_count

        if self.total_mark_items_count is not None:
            result['TotalMarkItemsCount'] = self.total_mark_items_count

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptedMarkItemsCount') is not None:
            self.accepted_mark_items_count = m.get('AcceptedMarkItemsCount')

        if m.get('CheckCount') is not None:
            self.check_count = m.get('CheckCount')

        if m.get('CheckedAcceptedCount') is not None:
            self.checked_accepted_count = m.get('CheckedAcceptedCount')

        if m.get('CheckedAccuracy') is not None:
            self.checked_accuracy = m.get('CheckedAccuracy')

        if m.get('MarkEfficiency') is not None:
            self.mark_efficiency = m.get('MarkEfficiency')

        if m.get('MarkTime') is not None:
            self.mark_time = m.get('MarkTime')

        if m.get('SamplingAccuracy') is not None:
            self.sampling_accuracy = m.get('SamplingAccuracy')

        if m.get('SamplingCount') is not None:
            self.sampling_count = m.get('SamplingCount')

        if m.get('SamplingErrorCount') is not None:
            self.sampling_error_count = m.get('SamplingErrorCount')

        if m.get('TotalMarkItemsCount') is not None:
            self.total_mark_items_count = m.get('TotalMarkItemsCount')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

