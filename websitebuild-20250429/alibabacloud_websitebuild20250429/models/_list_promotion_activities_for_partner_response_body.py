# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListPromotionActivitiesForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: main_models.ListPromotionActivitiesForPartnerResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The access denied detail.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message.
        self.dynamic_message = dynamic_message
        # The error arguments.
        self.error_args = error_args
        # The number of entries per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The response data.
        self.module = module
        # The token for the next query. This parameter is empty if no more results exist.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The root error message.
        self.root_error_msg = root_error_msg
        # Indicates whether the request is processed synchronously.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.ListPromotionActivitiesForPartnerResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListPromotionActivitiesForPartnerResponseBodyModule(DaraModel):
    def __init__(
        self,
        activities: List[main_models.ListPromotionActivitiesForPartnerResponseBodyModuleActivities] = None,
        total_count: int = None,
    ):
        # The list of promotional activities.
        self.activities = activities
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.activities:
            for v1 in self.activities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Activities'] = []
        if self.activities is not None:
            for k1 in self.activities:
                result['Activities'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activities = []
        if m.get('Activities') is not None:
            for k1 in m.get('Activities'):
                temp_model = main_models.ListPromotionActivitiesForPartnerResponseBodyModuleActivities()
                self.activities.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPromotionActivitiesForPartnerResponseBodyModuleActivities(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_name: str = None,
        activity_type: str = None,
        consumed_quota: int = None,
        create_time: str = None,
        created_by: str = None,
        eligibility_config: str = None,
        end_date: str = None,
        offer_config: str = None,
        offer_config_summary: str = None,
        remaining_quota: int = None,
        start_date: str = None,
        status: str = None,
        total_quota: int = None,
        touchpoint_config: str = None,
        update_time: str = None,
        updated_by: str = None,
        warning_threshold: int = None,
    ):
        # The activity code.
        self.activity_code = activity_code
        # The activity name.
        self.activity_name = activity_name
        # The activity type.
        self.activity_type = activity_type
        # The consumed quota.
        self.consumed_quota = consumed_quota
        # The creation time.
        self.create_time = create_time
        # The creator.
        self.created_by = created_by
        # The eligibility configuration (JSON).
        self.eligibility_config = eligibility_config
        # The end date.
        self.end_date = end_date
        # The offer configuration (JSON).
        self.offer_config = offer_config
        # The offer configuration summary.
        self.offer_config_summary = offer_config_summary
        # The remaining quota.
        self.remaining_quota = remaining_quota
        # The start date.
        self.start_date = start_date
        # The activity status.
        self.status = status
        # The total quota.
        self.total_quota = total_quota
        # The touchpoint configuration (JSON).
        self.touchpoint_config = touchpoint_config
        # The update time.
        self.update_time = update_time
        # The user who last updated the activity.
        self.updated_by = updated_by
        # The warning threshold.
        self.warning_threshold = warning_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.consumed_quota is not None:
            result['ConsumedQuota'] = self.consumed_quota

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.eligibility_config is not None:
            result['EligibilityConfig'] = self.eligibility_config

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.offer_config is not None:
            result['OfferConfig'] = self.offer_config

        if self.offer_config_summary is not None:
            result['OfferConfigSummary'] = self.offer_config_summary

        if self.remaining_quota is not None:
            result['RemainingQuota'] = self.remaining_quota

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.touchpoint_config is not None:
            result['TouchpointConfig'] = self.touchpoint_config

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.warning_threshold is not None:
            result['WarningThreshold'] = self.warning_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('ConsumedQuota') is not None:
            self.consumed_quota = m.get('ConsumedQuota')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('EligibilityConfig') is not None:
            self.eligibility_config = m.get('EligibilityConfig')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('OfferConfig') is not None:
            self.offer_config = m.get('OfferConfig')

        if m.get('OfferConfigSummary') is not None:
            self.offer_config_summary = m.get('OfferConfigSummary')

        if m.get('RemainingQuota') is not None:
            self.remaining_quota = m.get('RemainingQuota')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('TouchpointConfig') is not None:
            self.touchpoint_config = m.get('TouchpointConfig')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('WarningThreshold') is not None:
            self.warning_threshold = m.get('WarningThreshold')

        return self

