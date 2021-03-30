# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateDeliveryHistoryJobRequest(TeaModel):
    def __init__(
        self,
        trail_name: str = None,
        client_token: str = None,
    ):
        self.trail_name = trail_name
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trail_name is not None:
            result['TrailName'] = self.trail_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDeliveryHistoryJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: int = None,
    ):
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateDeliveryHistoryJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeliveryHistoryJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDeliveryHistoryJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrailRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        event_rw: str = None,
        trail_region: str = None,
        is_organization_trail: bool = None,
    ):
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_key_prefix = oss_key_prefix
        self.oss_write_role_arn = oss_write_role_arn
        self.sls_project_arn = sls_project_arn
        self.sls_write_role_arn = sls_write_role_arn
        self.event_rw = event_rw
        self.trail_region = trail_region
        self.is_organization_trail = is_organization_trail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')
        return self


class CreateTrailResponseBody(TeaModel):
    def __init__(
        self,
        sls_project_arn: str = None,
        oss_write_role_arn: str = None,
        event_rw: str = None,
        request_id: str = None,
        home_region: str = None,
        oss_key_prefix: str = None,
        oss_bucket_name: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
        name: str = None,
    ):
        self.sls_project_arn = sls_project_arn
        self.oss_write_role_arn = oss_write_role_arn
        self.event_rw = event_rw
        self.request_id = request_id
        self.home_region = home_region
        self.oss_key_prefix = oss_key_prefix
        self.oss_bucket_name = oss_bucket_name
        self.sls_write_role_arn = sls_write_role_arn
        self.trail_region = trail_region
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTrailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeliveryHistoryJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteDeliveryHistoryJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeliveryHistoryJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeliveryHistoryJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeliveryHistoryJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrailRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteTrailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTrailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_endpoint: str = None,
        local_name: str = None,
    ):
        self.region_id = region_id
        self.region_endpoint = region_endpoint
        self.local_name = local_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrailsRequest(TeaModel):
    def __init__(
        self,
        include_shadow_trails: bool = None,
        name_list: str = None,
        include_organization_trail: bool = None,
    ):
        self.include_shadow_trails = include_shadow_trails
        self.name_list = name_list
        self.include_organization_trail = include_organization_trail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_shadow_trails is not None:
            result['IncludeShadowTrails'] = self.include_shadow_trails
        if self.name_list is not None:
            result['NameList'] = self.name_list
        if self.include_organization_trail is not None:
            result['IncludeOrganizationTrail'] = self.include_organization_trail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeShadowTrails') is not None:
            self.include_shadow_trails = m.get('IncludeShadowTrails')
        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')
        if m.get('IncludeOrganizationTrail') is not None:
            self.include_organization_trail = m.get('IncludeOrganizationTrail')
        return self


class DescribeTrailsResponseBodyTrailList(TeaModel):
    def __init__(
        self,
        trail_region: str = None,
        status: str = None,
        update_time: str = None,
        home_region: str = None,
        create_time: str = None,
        oss_key_prefix: str = None,
        event_rw: str = None,
        start_logging_time: str = None,
        oss_write_role_arn: str = None,
        sls_project_arn: str = None,
        is_organization_trail: bool = None,
        sls_write_role_arn: str = None,
        stop_logging_time: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        region: str = None,
        organization_id: str = None,
        is_shadow_trail: int = None,
        oss_bucket_location: str = None,
    ):
        self.trail_region = trail_region
        self.status = status
        self.update_time = update_time
        self.home_region = home_region
        self.create_time = create_time
        self.oss_key_prefix = oss_key_prefix
        self.event_rw = event_rw
        self.start_logging_time = start_logging_time
        self.oss_write_role_arn = oss_write_role_arn
        self.sls_project_arn = sls_project_arn
        self.is_organization_trail = is_organization_trail
        self.sls_write_role_arn = sls_write_role_arn
        self.stop_logging_time = stop_logging_time
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.region = region
        self.organization_id = organization_id
        self.is_shadow_trail = is_shadow_trail
        self.oss_bucket_location = oss_bucket_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.region is not None:
            result['Region'] = self.region
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.is_shadow_trail is not None:
            result['IsShadowTrail'] = self.is_shadow_trail
        if self.oss_bucket_location is not None:
            result['OssBucketLocation'] = self.oss_bucket_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('IsShadowTrail') is not None:
            self.is_shadow_trail = m.get('IsShadowTrail')
        if m.get('OssBucketLocation') is not None:
            self.oss_bucket_location = m.get('OssBucketLocation')
        return self


class DescribeTrailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trail_list: List[DescribeTrailsResponseBodyTrailList] = None,
    ):
        self.request_id = request_id
        self.trail_list = trail_list

    def validate(self):
        if self.trail_list:
            for k in self.trail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrailList'] = []
        if self.trail_list is not None:
            for k in self.trail_list:
                result['TrailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trail_list = []
        if m.get('TrailList') is not None:
            for k in m.get('TrailList'):
                temp_model = DescribeTrailsResponseBodyTrailList()
                self.trail_list.append(temp_model.from_map(k))
        return self


class DescribeTrailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTrailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTrailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrailStatusRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        is_organization_trail: bool = None,
    ):
        self.name = name
        self.is_organization_trail = is_organization_trail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')
        return self


class GetTrailStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        start_logging_time: str = None,
        latest_delivery_error: str = None,
        stop_logging_time: str = None,
        is_logging: bool = None,
        latest_delivery_time: str = None,
        latest_delivery_log_service_error: str = None,
        latest_delivery_log_service_time: str = None,
        oss_bucket_status: bool = None,
        sls_log_store_status: bool = None,
    ):
        self.request_id = request_id
        self.start_logging_time = start_logging_time
        self.latest_delivery_error = latest_delivery_error
        self.stop_logging_time = stop_logging_time
        self.is_logging = is_logging
        self.latest_delivery_time = latest_delivery_time
        self.latest_delivery_log_service_error = latest_delivery_log_service_error
        self.latest_delivery_log_service_time = latest_delivery_log_service_time
        self.oss_bucket_status = oss_bucket_status
        self.sls_log_store_status = sls_log_store_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time
        if self.latest_delivery_error is not None:
            result['LatestDeliveryError'] = self.latest_delivery_error
        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time
        if self.is_logging is not None:
            result['IsLogging'] = self.is_logging
        if self.latest_delivery_time is not None:
            result['LatestDeliveryTime'] = self.latest_delivery_time
        if self.latest_delivery_log_service_error is not None:
            result['LatestDeliveryLogServiceError'] = self.latest_delivery_log_service_error
        if self.latest_delivery_log_service_time is not None:
            result['LatestDeliveryLogServiceTime'] = self.latest_delivery_log_service_time
        if self.oss_bucket_status is not None:
            result['OssBucketStatus'] = self.oss_bucket_status
        if self.sls_log_store_status is not None:
            result['SlsLogStoreStatus'] = self.sls_log_store_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')
        if m.get('LatestDeliveryError') is not None:
            self.latest_delivery_error = m.get('LatestDeliveryError')
        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')
        if m.get('IsLogging') is not None:
            self.is_logging = m.get('IsLogging')
        if m.get('LatestDeliveryTime') is not None:
            self.latest_delivery_time = m.get('LatestDeliveryTime')
        if m.get('LatestDeliveryLogServiceError') is not None:
            self.latest_delivery_log_service_error = m.get('LatestDeliveryLogServiceError')
        if m.get('LatestDeliveryLogServiceTime') is not None:
            self.latest_delivery_log_service_time = m.get('LatestDeliveryLogServiceTime')
        if m.get('OssBucketStatus') is not None:
            self.oss_bucket_status = m.get('OssBucketStatus')
        if m.get('SlsLogStoreStatus') is not None:
            self.sls_log_store_status = m.get('SlsLogStoreStatus')
        return self


class GetTrailStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrailStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTrailStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeliveryHistoryJobsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs(TeaModel):
    def __init__(
        self,
        trail_name: str = None,
        end_time: str = None,
        start_time: str = None,
        job_status: int = None,
        home_region: str = None,
        updated_time: str = None,
        job_id: int = None,
        created_time: str = None,
    ):
        self.trail_name = trail_name
        self.end_time = end_time
        self.start_time = start_time
        self.job_status = job_status
        self.home_region = home_region
        self.updated_time = updated_time
        self.job_id = job_id
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trail_name is not None:
            result['TrailName'] = self.trail_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class ListDeliveryHistoryJobsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        delivery_history_jobs: List[ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.delivery_history_jobs = delivery_history_jobs

    def validate(self):
        if self.delivery_history_jobs:
            for k in self.delivery_history_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['DeliveryHistoryJobs'] = []
        if self.delivery_history_jobs is not None:
            for k in self.delivery_history_jobs:
                result['DeliveryHistoryJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.delivery_history_jobs = []
        if m.get('DeliveryHistoryJobs') is not None:
            for k in m.get('DeliveryHistoryJobs'):
                temp_model = ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs()
                self.delivery_history_jobs.append(temp_model.from_map(k))
        return self


class ListDeliveryHistoryJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeliveryHistoryJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeliveryHistoryJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LookupEventsRequestLookupAttribute(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LookupEventsRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: str = None,
        start_time: str = None,
        end_time: str = None,
        direction: str = None,
        lookup_attribute: List[LookupEventsRequestLookupAttribute] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.start_time = start_time
        self.end_time = end_time
        self.direction = direction
        self.lookup_attribute = lookup_attribute

    def validate(self):
        if self.lookup_attribute:
            for k in self.lookup_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.direction is not None:
            result['Direction'] = self.direction
        result['LookupAttribute'] = []
        if self.lookup_attribute is not None:
            for k in self.lookup_attribute:
                result['LookupAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        self.lookup_attribute = []
        if m.get('LookupAttribute') is not None:
            for k in m.get('LookupAttribute'):
                temp_model = LookupEventsRequestLookupAttribute()
                self.lookup_attribute.append(temp_model.from_map(k))
        return self


class LookupEventsResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        next_token: str = None,
        request_id: str = None,
        events: List[Dict[str, Any]] = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.next_token = next_token
        self.request_id = request_id
        self.events = events
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.events is not None:
            result['Events'] = self.events
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class LookupEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LookupEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LookupEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartLoggingRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class StartLoggingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartLoggingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLoggingRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class StopLoggingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopLoggingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrailRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        event_rw: str = None,
        trail_region: str = None,
    ):
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_key_prefix = oss_key_prefix
        self.oss_write_role_arn = oss_write_role_arn
        self.sls_project_arn = sls_project_arn
        self.sls_write_role_arn = sls_write_role_arn
        self.event_rw = event_rw
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        return self


class UpdateTrailResponseBody(TeaModel):
    def __init__(
        self,
        sls_project_arn: str = None,
        oss_write_role_arn: str = None,
        event_rw: str = None,
        request_id: str = None,
        home_region: str = None,
        oss_key_prefix: str = None,
        oss_bucket_name: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
        name: str = None,
    ):
        self.sls_project_arn = sls_project_arn
        self.oss_write_role_arn = oss_write_role_arn
        self.event_rw = event_rw
        self.request_id = request_id
        self.home_region = home_region
        self.oss_key_prefix = oss_key_prefix
        self.oss_bucket_name = oss_bucket_name
        self.sls_write_role_arn = sls_write_role_arn
        self.trail_region = trail_region
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTrailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


