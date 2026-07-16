# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TaskStatistic(DaraModel):
    def __init__(
        self,
        accept_item_count: float = None,
        check_abandon: float = None,
        check_accuracy: float = None,
        check_efficiency: float = None,
        checked_accuracy: float = None,
        checked_error: float = None,
        checked_reject_count: float = None,
        final_abandon_count: float = None,
        finished_item_count: int = None,
        finished_subtask_count: int = None,
        mark_efficiency: float = None,
        pre_mark_fixed_count: float = None,
        sampled_accuracy: float = None,
        sampled_error_count: float = None,
        sampled_reject_count: float = None,
        sampling_accuracy: float = None,
        total_check_count: float = None,
        total_check_time: float = None,
        total_checked_count: float = None,
        total_item_count: int = None,
        total_mark_time: float = None,
        total_sampled_count: float = None,
        total_sampling_count: float = None,
        total_subtask_count: int = None,
        total_work_time: float = None,
    ):
        # Data items that passed
        self.accept_item_count = accept_item_count
        # Quantity abandoned in the check flow
        self.check_abandon = check_abandon
        # Inspection accuracy
        self.check_accuracy = check_accuracy
        # Inspection efficiency (items/hour)
        self.check_efficiency = check_efficiency
        # Check accuracy
        self.checked_accuracy = checked_accuracy
        # Number of errors found in the inspection flow
        self.checked_error = checked_error
        # Number of checks
        self.checked_reject_count = checked_reject_count
        # Discarded data items
        self.final_abandon_count = final_abandon_count
        # Completed data items
        self.finished_item_count = finished_item_count
        # Quantity of completed subtasks
        self.finished_subtask_count = finished_subtask_count
        # Annotation efficiency (items/hour)
        self.mark_efficiency = mark_efficiency
        # Quantity of corrections made during pre-annotation
        self.pre_mark_fixed_count = pre_mark_fixed_count
        # Sampling accuracy
        self.sampled_accuracy = sampled_accuracy
        # Number of sampled fault samples
        self.sampled_error_count = sampled_error_count
        # Number of samples denied
        self.sampled_reject_count = sampled_reject_count
        # Sampling accuracy
        self.sampling_accuracy = sampling_accuracy
        # Total number of check flow steps
        self.total_check_count = total_check_count
        # Total check time (hours)
        self.total_check_time = total_check_time
        # Total number of checks
        self.total_checked_count = total_checked_count
        # Total number of data items
        self.total_item_count = total_item_count
        # Total time spent in the annotation phase (hours)
        self.total_mark_time = total_mark_time
        # Total sampling quantity
        self.total_sampled_count = total_sampled_count
        # Total number of sampled validations
        self.total_sampling_count = total_sampling_count
        # Total number of subtasks
        self.total_subtask_count = total_subtask_count
        # Total work time (hours)
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_item_count is not None:
            result['AcceptItemCount'] = self.accept_item_count

        if self.check_abandon is not None:
            result['CheckAbandon'] = self.check_abandon

        if self.check_accuracy is not None:
            result['CheckAccuracy'] = self.check_accuracy

        if self.check_efficiency is not None:
            result['CheckEfficiency'] = self.check_efficiency

        if self.checked_accuracy is not None:
            result['CheckedAccuracy'] = self.checked_accuracy

        if self.checked_error is not None:
            result['CheckedError'] = self.checked_error

        if self.checked_reject_count is not None:
            result['CheckedRejectCount'] = self.checked_reject_count

        if self.final_abandon_count is not None:
            result['FinalAbandonCount'] = self.final_abandon_count

        if self.finished_item_count is not None:
            result['FinishedItemCount'] = self.finished_item_count

        if self.finished_subtask_count is not None:
            result['FinishedSubtaskCount'] = self.finished_subtask_count

        if self.mark_efficiency is not None:
            result['MarkEfficiency'] = self.mark_efficiency

        if self.pre_mark_fixed_count is not None:
            result['PreMarkFixedCount'] = self.pre_mark_fixed_count

        if self.sampled_accuracy is not None:
            result['SampledAccuracy'] = self.sampled_accuracy

        if self.sampled_error_count is not None:
            result['SampledErrorCount'] = self.sampled_error_count

        if self.sampled_reject_count is not None:
            result['SampledRejectCount'] = self.sampled_reject_count

        if self.sampling_accuracy is not None:
            result['SamplingAccuracy'] = self.sampling_accuracy

        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count

        if self.total_check_time is not None:
            result['TotalCheckTime'] = self.total_check_time

        if self.total_checked_count is not None:
            result['TotalCheckedCount'] = self.total_checked_count

        if self.total_item_count is not None:
            result['TotalItemCount'] = self.total_item_count

        if self.total_mark_time is not None:
            result['TotalMarkTime'] = self.total_mark_time

        if self.total_sampled_count is not None:
            result['TotalSampledCount'] = self.total_sampled_count

        if self.total_sampling_count is not None:
            result['TotalSamplingCount'] = self.total_sampling_count

        if self.total_subtask_count is not None:
            result['TotalSubtaskCount'] = self.total_subtask_count

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptItemCount') is not None:
            self.accept_item_count = m.get('AcceptItemCount')

        if m.get('CheckAbandon') is not None:
            self.check_abandon = m.get('CheckAbandon')

        if m.get('CheckAccuracy') is not None:
            self.check_accuracy = m.get('CheckAccuracy')

        if m.get('CheckEfficiency') is not None:
            self.check_efficiency = m.get('CheckEfficiency')

        if m.get('CheckedAccuracy') is not None:
            self.checked_accuracy = m.get('CheckedAccuracy')

        if m.get('CheckedError') is not None:
            self.checked_error = m.get('CheckedError')

        if m.get('CheckedRejectCount') is not None:
            self.checked_reject_count = m.get('CheckedRejectCount')

        if m.get('FinalAbandonCount') is not None:
            self.final_abandon_count = m.get('FinalAbandonCount')

        if m.get('FinishedItemCount') is not None:
            self.finished_item_count = m.get('FinishedItemCount')

        if m.get('FinishedSubtaskCount') is not None:
            self.finished_subtask_count = m.get('FinishedSubtaskCount')

        if m.get('MarkEfficiency') is not None:
            self.mark_efficiency = m.get('MarkEfficiency')

        if m.get('PreMarkFixedCount') is not None:
            self.pre_mark_fixed_count = m.get('PreMarkFixedCount')

        if m.get('SampledAccuracy') is not None:
            self.sampled_accuracy = m.get('SampledAccuracy')

        if m.get('SampledErrorCount') is not None:
            self.sampled_error_count = m.get('SampledErrorCount')

        if m.get('SampledRejectCount') is not None:
            self.sampled_reject_count = m.get('SampledRejectCount')

        if m.get('SamplingAccuracy') is not None:
            self.sampling_accuracy = m.get('SamplingAccuracy')

        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')

        if m.get('TotalCheckTime') is not None:
            self.total_check_time = m.get('TotalCheckTime')

        if m.get('TotalCheckedCount') is not None:
            self.total_checked_count = m.get('TotalCheckedCount')

        if m.get('TotalItemCount') is not None:
            self.total_item_count = m.get('TotalItemCount')

        if m.get('TotalMarkTime') is not None:
            self.total_mark_time = m.get('TotalMarkTime')

        if m.get('TotalSampledCount') is not None:
            self.total_sampled_count = m.get('TotalSampledCount')

        if m.get('TotalSamplingCount') is not None:
            self.total_sampling_count = m.get('TotalSamplingCount')

        if m.get('TotalSubtaskCount') is not None:
            self.total_subtask_count = m.get('TotalSubtaskCount')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

