# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class ListDeliveryHistoryJobsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class ListDeliveryHistoryJobsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, delivery_history_jobs=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.delivery_history_jobs = delivery_history_jobs  # type: List[ListDeliveryHistoryJobsResponseDeliveryHistoryJobs]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.delivery_history_jobs, 'delivery_history_jobs')
        if self.delivery_history_jobs:
            for k in self.delivery_history_jobs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['DeliveryHistoryJobs'] = []
        if self.delivery_history_jobs is not None:
            for k in self.delivery_history_jobs:
                result['DeliveryHistoryJobs'].append(k.to_map() if k else None)
        else:
            result['DeliveryHistoryJobs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.delivery_history_jobs = []
        if map.get('DeliveryHistoryJobs') is not None:
            for k in map.get('DeliveryHistoryJobs'):
                temp_model = ListDeliveryHistoryJobsResponseDeliveryHistoryJobs()
                self.delivery_history_jobs.append(temp_model.from_map(k))
        else:
            self.delivery_history_jobs = None
        return self


class ListDeliveryHistoryJobsResponseDeliveryHistoryJobs(TeaModel):
    def __init__(self, trail_name=None, created_time=None, updated_time=None, home_region=None):
        self.trail_name = trail_name    # type: str
        self.created_time = created_time  # type: str
        self.updated_time = updated_time  # type: str
        self.home_region = home_region  # type: str

    def validate(self):
        self.validate_required(self.trail_name, 'trail_name')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.updated_time, 'updated_time')
        self.validate_required(self.home_region, 'home_region')

    def to_map(self):
        result = {}
        result['TrailName'] = self.trail_name
        result['CreatedTime'] = self.created_time
        result['UpdatedTime'] = self.updated_time
        result['HomeRegion'] = self.home_region
        return result

    def from_map(self, map={}):
        self.trail_name = map.get('TrailName')
        self.created_time = map.get('CreatedTime')
        self.updated_time = map.get('UpdatedTime')
        self.home_region = map.get('HomeRegion')
        return self


class CreateDeliveryHistoryJobRequest(TeaModel):
    def __init__(self, trail_name=None, client_token=None):
        self.trail_name = trail_name    # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.trail_name, 'trail_name')

    def to_map(self):
        result = {}
        result['TrailName'] = self.trail_name
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.trail_name = map.get('TrailName')
        self.client_token = map.get('ClientToken')
        return self


class CreateDeliveryHistoryJobResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class LookupEventsRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, start_time=None, end_time=None, lookup_attribute=None,
                 direction=None):
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.lookup_attribute = lookup_attribute  # type: List[LookupEventsRequestLookupAttribute]
        self.direction = direction      # type: str

    def validate(self):
        if self.lookup_attribute:
            for k in self.lookup_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['LookupAttribute'] = []
        if self.lookup_attribute is not None:
            for k in self.lookup_attribute:
                result['LookupAttribute'].append(k.to_map() if k else None)
        else:
            result['LookupAttribute'] = None
        result['Direction'] = self.direction
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.lookup_attribute = []
        if map.get('LookupAttribute') is not None:
            for k in map.get('LookupAttribute'):
                temp_model = LookupEventsRequestLookupAttribute()
                self.lookup_attribute.append(temp_model.from_map(k))
        else:
            self.lookup_attribute = None
        self.direction = map.get('Direction')
        return self


class LookupEventsRequestLookupAttribute(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class LookupEventsResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, start_time=None, end_time=None, events=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.events = events            # type: List[Dict[str, Any]]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.events, 'events')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Events'] = self.events
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.events = map.get('Events')
        return self
