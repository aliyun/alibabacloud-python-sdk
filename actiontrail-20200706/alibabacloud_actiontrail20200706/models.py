# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateDeliveryHistoryJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        trail_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # The token can contain only ASCII characters and can be up to 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The name of the trail for which you want to create a historical event delivery task.
        self.trail_name = trail_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.trail_name is not None:
            result['TrailName'] = self.trail_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')
        return self


class CreateDeliveryHistoryJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        request_id: str = None,
    ):
        # The ID of the historical event delivery task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeliveryHistoryJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeliveryHistoryJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeliveryHistoryJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrailRequest(TeaModel):
    def __init__(
        self,
        event_rw: str = None,
        is_organization_trail: bool = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
    ):
        # The read/write type of the events to be delivered. Valid values:
        # 
        # *   Write: write events. It is the default value.
        # *   Read: read events.
        # *   All: read and write events.
        self.event_rw = event_rw
        # Specifies whether to create a multi-account trail. Valid values:
        # 
        # *   true: creates a multi-account trail.
        # *   false (default): creates a single-account trail.
        self.is_organization_trail = is_organization_trail
        # The name of the trail to be created.
        # 
        # The name must be 6 to 36 characters in length. The name must start with a lowercase letter and can contain lowercase letters, digits, hyphens (-), and underscores (\_).
        # 
        # > The name must be unique within your Alibaba Cloud account.
        self.name = name
        # The name of the OSS bucket to which events are to be delivered.
        # 
        # The name must be 3 to 63 characters in length. The name must start with a lowercase letter or a digit and can contain lowercase letters, digits, and hyphens (-).
        # 
        # > You must specify at least one of the OssBucketName and SlsProjectArn parameters.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the log files to be stored in the destination OSS bucket. This parameter can be left empty.
        # 
        # The prefix must be 6 to 32 characters in length. The prefix must start with a letter and can contain letters, digits, hyphens (-), forward slashes (/), and underscores (\_).
        self.oss_key_prefix = oss_key_prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        # 
        # *   If you do not specify this parameter, ActionTrail creates a service-linked role to create the required resources. For more information, see [Manage the service-linked role](~~169244~~).
        # *   If you specify this parameter, you must grant the permissions of the service-linked role that is assumed by ActionTrail to the RAM role before you can deliver events to your Alibaba Cloud account. If you need to deliver events to other Alibaba Cloud accounts, you must attach the permission policy that is used to grant permissions related to event delivery to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](~~207462~~).
        self.oss_write_role_arn = oss_write_role_arn
        # The ARN of the Log Service project to which events are to be delivered.
        # 
        # > You must specify at least one of the OssBucketName and SlsProjectArn parameters.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the Log Service project.
        # 
        # *   If you do not specify this parameter, ActionTrail creates a service-linked role to create the corresponding resource. For more information, see [Manage the service-linked role](~~169244~~).
        # *   If you specify this parameter, you must grant the permissions of the service-linked role that is assumed by ActionTrail to the RAM role before you can deliver events to your Alibaba Cloud account. If you need to deliver events to other Alibaba Cloud accounts, you must attach the permission policy that is used to grant permissions related to event delivery to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](~~207462~~).
        self.sls_write_role_arn = sls_write_role_arn
        # The one or more regions from which the trail delivers events.
        # 
        # The default value is All, which indicates that the trail delivers events from all regions.
        # 
        # You can also specify specific regions. You can call the [DescribeRegions](~~213597~~) operation to query all the supported regions.
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail
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
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')
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
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        return self


class CreateTrailResponseBody(TeaModel):
    def __init__(
        self,
        event_rw: str = None,
        home_region: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        request_id: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
    ):
        # The read/write type of the events to be delivered.
        self.event_rw = event_rw
        # The home region of the trail.
        self.home_region = home_region
        # The name of the trail.
        self.name = name
        # The name of the OSS bucket to which events are to be delivered.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the log files to be stored in the destination OSS bucket.
        self.oss_key_prefix = oss_key_prefix
        # The ARN of the service-linked role that is assumed by ActionTrail to deliver events to the destination OSS bucket.
        self.oss_write_role_arn = oss_write_role_arn
        # The ID of the request.
        self.request_id = request_id
        # The ARN of the Log Service project to which events are to be delivered.
        self.sls_project_arn = sls_project_arn
        # The ARN of the service-linked role that is assumed by ActionTrail to deliver events to the destination Log Service project.
        self.sls_write_role_arn = sls_write_role_arn
        # The one or more regions from which the trail delivers events.
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        return self


class CreateTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeliveryHistoryJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the historical event delivery task to be deleted.
        # 
        # You can call the [ListDeliveryHistoryJobs](~~188101~~) operation to query task IDs.
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
        # The ID of the request.
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
        status_code: int = None,
        body: DeleteDeliveryHistoryJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDeliveryHistoryJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrailRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the trail that you want to delete.
        # 
        # The name must be 6 to 36 characters in length. The name must start with a lowercase letter and can contain lowercase letters, digits, hyphens (-), and underscores (\_).
        # 
        # > The name must be unique within your Alibaba Cloud account.
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
        # The ID of the request.
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
        status_code: int = None,
        body: DeleteTrailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The language in which the region names are returned. Valid values:
        # 
        # - zh-CN: Chinese.
        # - en-US: English. It is the default value.
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
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        # 
        # > If the AcceptLanguage parameter is set to zh-CN, the Chinese name of the region is returned. If the AcceptLanguage parameter is set to zh-US or left empty, the English name of the region is returned.
        self.local_name = local_name
        # The endpoint of ActionTrail in the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The regions returned.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrailsRequest(TeaModel):
    def __init__(
        self,
        include_organization_trail: bool = None,
        include_shadow_trails: bool = None,
        name_list: str = None,
    ):
        # Specifies whether to query the information about multi-account trails. Valid values:
        # 
        # *   true
        # *   false (default)
        self.include_organization_trail = include_organization_trail
        # Specifies whether to return the information about shadow trails. Valid values:
        # 
        # *   false: Do not return the information about shadow trails. It is the default value.
        # *   true: Return the information about shadow trails.
        self.include_shadow_trails = include_shadow_trails
        # The names of the trails whose information you want to query. Separate multiple trail names with commas (,).
        self.name_list = name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_organization_trail is not None:
            result['IncludeOrganizationTrail'] = self.include_organization_trail
        if self.include_shadow_trails is not None:
            result['IncludeShadowTrails'] = self.include_shadow_trails
        if self.name_list is not None:
            result['NameList'] = self.name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeOrganizationTrail') is not None:
            self.include_organization_trail = m.get('IncludeOrganizationTrail')
        if m.get('IncludeShadowTrails') is not None:
            self.include_shadow_trails = m.get('IncludeShadowTrails')
        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')
        return self


class DescribeTrailsResponseBodyTrailList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        event_rw: str = None,
        home_region: str = None,
        is_organization_trail: bool = None,
        name: str = None,
        organization_id: str = None,
        oss_bucket_location: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        region: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        start_logging_time: str = None,
        status: str = None,
        stop_logging_time: str = None,
        trail_arn: str = None,
        trail_region: str = None,
        update_time: str = None,
    ):
        # The time when the trail was created.
        self.create_time = create_time
        # The read/write type of the events that are delivered. Valid values:
        # 
        # *   Write: write events. This is the default value.
        # *   Read: read events.
        # *   All: read and write events.
        self.event_rw = event_rw
        # The home region of the trail.
        self.home_region = home_region
        # Indicates whether the trail is a multi-account trail. Valid values:
        # 
        # *   false (default)
        # *   true
        self.is_organization_trail = is_organization_trail
        # The name of the trail.
        self.name = name
        # The ID of the resource directory.
        # 
        # >  This parameter is returned only when the trail is a multi-account trail.
        self.organization_id = organization_id
        # The region where the OSS bucket resides.
        self.oss_bucket_location = oss_bucket_location
        # The name of the OSS bucket to which events are delivered.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the files that are stored in the Object Storage Service (OSS) bucket.
        self.oss_key_prefix = oss_key_prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        self.oss_write_role_arn = oss_write_role_arn
        # The region where the trail resides.
        self.region = region
        # The ARN of the Log Service project to which events are delivered.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the Log Service project.
        self.sls_write_role_arn = sls_write_role_arn
        # The time when the trail was last enabled.
        self.start_logging_time = start_logging_time
        # The status of the trail. Valid values:
        # 
        # *   Disable: disabled.
        # *   Enable: enabled.
        # *   Fresh: The trail is created but is not enabled.
        self.status = status
        # The time when the trail was last disabled.
        self.stop_logging_time = stop_logging_time
        # The ARN of the trail.
        self.trail_arn = trail_arn
        # The region of the trail.
        self.trail_region = trail_region
        # The time when the configurations of the trail were last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail
        if self.name is not None:
            result['Name'] = self.name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.oss_bucket_location is not None:
            result['OssBucketLocation'] = self.oss_bucket_location
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.region is not None:
            result['Region'] = self.region
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time
        if self.trail_arn is not None:
            result['TrailArn'] = self.trail_arn
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OssBucketLocation') is not None:
            self.oss_bucket_location = m.get('OssBucketLocation')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')
        if m.get('TrailArn') is not None:
            self.trail_arn = m.get('TrailArn')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTrailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trail_list: List[DescribeTrailsResponseBodyTrailList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # A list of returned trails.
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
        status_code: int = None,
        body: DescribeTrailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedEventsRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        next_token: str = None,
        page_size: str = None,
        service_name: str = None,
    ):
        # The AccessKey ID.
        self.access_key = access_key
        # The token that determines the start point of the query.
        # 
        # > The request parameters must be the same as those of the last request.
        self.next_token = next_token
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 100.
        # 
        # Default value: 20.
        self.page_size = page_size
        # The Alibaba Cloud service. For more information about the Alibaba Cloud services supported by ActionTrail, see [Supported Alibaba Cloud services](~~28829~~).
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetAccessKeyLastUsedEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        detail: str = None,
        event_name: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # An array that consists of the details about the event.
        self.detail = detail
        # The name of the event.
        self.event_name = event_name
        # The event source.
        self.source = source
        # The timestamp when the event was generated.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.source is not None:
            result['Source'] = self.source
        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')
        return self


class GetAccessKeyLastUsedEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[GetAccessKeyLastUsedEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of returned events.
        self.events = events
        # The token that determines the start point of the query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = GetAccessKeyLastUsedEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessKeyLastUsedEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedInfoRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        # The AccessKey secret.
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GetAccessKeyLastUsedInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        account_id: str = None,
        account_type: str = None,
        detail: str = None,
        owner_id: str = None,
        request_id: str = None,
        service_name: str = None,
        service_name_cn: str = None,
        service_name_en: str = None,
        source: str = None,
        used_timestamp: int = None,
        user_name: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The type of the account to which the AccessKey pair belongs.
        self.account_type = account_type
        # The details about the event.
        self.detail = detail
        # The ID of the account to which the AccessKey pair belongs.
        self.owner_id = owner_id
        # The ID of the request.
        self.request_id = request_id
        # The Alibaba Cloud service that was last accessed.
        self.service_name = service_name
        # The Chinese name of the Alibaba Cloud service that was last accessed.
        self.service_name_cn = service_name_cn
        # The English name of the Alibaba Cloud service that was last accessed.
        self.service_name_en = service_name_en
        # The event source.
        self.source = source
        # The timestamp when the AccessKey pair was last called.
        self.used_timestamp = used_timestamp
        # The name of the account to which the AccessKey pair belongs.
        # 
        # If the value of the AccountType parameter is root-account, the value of the UserName parameter is root. If the value of the AccountType parameter is ram-user, the value of the UserName parameter is the name of a RAM user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_name_cn is not None:
            result['ServiceNameCn'] = self.service_name_cn
        if self.service_name_en is not None:
            result['ServiceNameEn'] = self.service_name_en
        if self.source is not None:
            result['Source'] = self.source
        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceNameCn') is not None:
            self.service_name_cn = m.get('ServiceNameCn')
        if m.get('ServiceNameEn') is not None:
            self.service_name_en = m.get('ServiceNameEn')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetAccessKeyLastUsedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessKeyLastUsedInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedIpsRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        next_token: str = None,
        page_size: str = None,
        service_name: str = None,
    ):
        # The AccessKey ID.
        self.access_key = access_key
        # The token that determines the start point of the query.
        # 
        # > The request parameters must be the same as those of the last request.
        self.next_token = next_token
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 100.
        # 
        # Default value: 20.
        self.page_size = page_size
        # The Alibaba Cloud service. For more information about the Alibaba Cloud services supported by ActionTrail, see [Supported Alibaba Cloud services](~~28829~~).
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetAccessKeyLastUsedIpsResponseBodyIps(TeaModel):
    def __init__(
        self,
        detail: str = None,
        ip: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # An array that consists of the details about the event.
        self.detail = detail
        # The IP address.
        self.ip = ip
        # The event source.
        self.source = source
        # The timestamp when the IP address was used.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source is not None:
            result['Source'] = self.source
        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')
        return self


class GetAccessKeyLastUsedIpsResponseBody(TeaModel):
    def __init__(
        self,
        ips: List[GetAccessKeyLastUsedIpsResponseBodyIps] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of returned IP addresses.
        self.ips = ips
        # The token that determines the start point of the query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = GetAccessKeyLastUsedIpsResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessKeyLastUsedIpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedProductsRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        # The AccessKey ID.
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GetAccessKeyLastUsedProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        detail: str = None,
        service_name: str = None,
        service_name_cn: str = None,
        service_name_en: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # The event details.
        self.detail = detail
        # The Alibaba Cloud service.
        self.service_name = service_name
        # The Chinese name of the Alibaba Cloud service.
        self.service_name_cn = service_name_cn
        # The English name of the Alibaba Cloud service.
        self.service_name_en = service_name_en
        # The event source.
        # 
        # Valid values:
        # 
        # *   Internal
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     other events
        # 
        #     <!-- -->
        # 
        # *   ManagementEvent
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     management events
        # 
        #     <!-- -->
        # 
        # *   DataEvent
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     data events
        # 
        #     <!-- -->
        self.source = source
        # A pagination token. It can be used in the next request to retrieve a new page of results. Unit: millisecond.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_name_cn is not None:
            result['ServiceNameCn'] = self.service_name_cn
        if self.service_name_en is not None:
            result['ServiceNameEn'] = self.service_name_en
        if self.source is not None:
            result['Source'] = self.source
        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceNameCn') is not None:
            self.service_name_cn = m.get('ServiceNameCn')
        if m.get('ServiceNameEn') is not None:
            self.service_name_en = m.get('ServiceNameEn')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')
        return self


class GetAccessKeyLastUsedProductsResponseBody(TeaModel):
    def __init__(
        self,
        products: List[GetAccessKeyLastUsedProductsResponseBodyProducts] = None,
        request_id: str = None,
    ):
        # The list of returned Alibaba Cloud services.
        self.products = products
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Products'] = []
        if self.products is not None:
            for k in self.products:
                result['Products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('Products') is not None:
            for k in m.get('Products'):
                temp_model = GetAccessKeyLastUsedProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessKeyLastUsedProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedResourcesRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        next_token: str = None,
        page_size: str = None,
        service_name: str = None,
    ):
        # The AccessKey ID.
        self.access_key = access_key
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # > The request parameters must be the same as those of the last request.
        self.next_token = next_token
        # The number of entries per page.
        # 
        # *   Valid values: 0 to 100.
        # *   Default value: 20.
        self.page_size = page_size
        # The Alibaba Cloud service. For more information about the Alibaba Cloud services supported by ActionTrail, see [Supported Alibaba Cloud services](~~28829~~).
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetAccessKeyLastUsedResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        detail: str = None,
        resource_name: str = None,
        resource_type: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # The event details.
        self.detail = detail
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type
        # The event source.
        # 
        # Valid values:
        # 
        # *   Internal
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     other events
        # 
        #     <!-- -->
        # 
        # *   ManagementEvent
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     management events
        # 
        #     <!-- -->
        # 
        # *   DataEvent
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     data events
        # 
        #     <!-- -->
        self.source = source
        # The timestamp when the resource was used. Unit: millisecond.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')
        return self


class GetAccessKeyLastUsedResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resources: List[GetAccessKeyLastUsedResourcesResponseBodyResources] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of returned resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = GetAccessKeyLastUsedResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class GetAccessKeyLastUsedResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessKeyLastUsedResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeliveryHistoryJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the historical event delivery task.
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


class GetDeliveryHistoryJobResponseBodyStatus(TeaModel):
    def __init__(
        self,
        region: str = None,
        status: int = None,
    ):
        # The ID of the region.
        self.region = region
        # The task status in each region. Valid values:
        # 
        # *   0: The task is initializing.
        # *   1: The task is delivering historical events.
        # *   2: The task is complete.
        # *   3: The task fails.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeliveryHistoryJobResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: str = None,
        home_region: str = None,
        job_id: int = None,
        job_status: int = None,
        request_id: str = None,
        start_time: str = None,
        status: List[GetDeliveryHistoryJobResponseBodyStatus] = None,
        trail_name: str = None,
        updated_time: str = None,
    ):
        # The time when the task was created.
        self.created_time = created_time
        # The time when the task ended.
        self.end_time = end_time
        # The home region of the trail.
        self.home_region = home_region
        # The ID of the task.
        self.job_id = job_id
        # The task status. Valid values:
        # 
        # *   0: The task is initializing.
        # *   1: The task is delivering historical events.
        # *   2: The task is complete.
        # *   3: The task fails.
        self.job_status = job_status
        # The ID of the request.
        self.request_id = request_id
        # The time when the task started.
        self.start_time = start_time
        # A list of task statuses in each region.
        self.status = status
        # The name of the trail based on which the task delivers events.
        self.trail_name = trail_name
        # The time when the task was updated.
        self.updated_time = updated_time

    def validate(self):
        if self.status:
            for k in self.status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Status'] = []
        if self.status is not None:
            for k in self.status:
                result['Status'].append(k.to_map() if k else None)
        if self.trail_name is not None:
            result['TrailName'] = self.trail_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.status = []
        if m.get('Status') is not None:
            for k in m.get('Status'):
                temp_model = GetDeliveryHistoryJobResponseBodyStatus()
                self.status.append(temp_model.from_map(k))
        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetDeliveryHistoryJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeliveryHistoryJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeliveryHistoryJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGlobalEventsStorageRegionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        storage_region: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The region where global events are stored.
        # 
        # Valid values:
        # 
        # *   ap-southeast-1
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     the Singapore region
        # 
        #     <!-- -->
        # 
        # *   cn-hangzhou
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     the China (Hangzhou) region
        # 
        #     <!-- -->
        self.storage_region = storage_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')
        return self


class GetGlobalEventsStorageRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGlobalEventsStorageRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGlobalEventsStorageRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrailStatusRequest(TeaModel):
    def __init__(
        self,
        is_organization_trail: bool = None,
        name: str = None,
    ):
        # Specifies whether to query the status of a multi-account trail. Valid values:
        # 
        # *   true: Query the status of a multi-account trail.
        # *   false: Query the status of a single-account trail. It is the default value.
        self.is_organization_trail = is_organization_trail
        # The name of the trail.
        # 
        # The name must be 6 to 36 characters in length. The name must start with a lowercase letter and can contain lowercase letters, digits, hyphens (-), and underscores (\_).
        # 
        # > The name must be unique within your Alibaba Cloud account.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetTrailStatusResponseBody(TeaModel):
    def __init__(
        self,
        is_logging: bool = None,
        latest_delivery_error: str = None,
        latest_delivery_log_service_error: str = None,
        latest_delivery_log_service_time: str = None,
        latest_delivery_time: str = None,
        oss_bucket_status: bool = None,
        request_id: str = None,
        sls_log_store_status: bool = None,
        start_logging_time: str = None,
        stop_logging_time: str = None,
    ):
        # Indicates whether logging is enabled for the trail. Valid values:
        # 
        # *   true
        # *   false
        self.is_logging = is_logging
        # The log of the last failed delivery.
        self.latest_delivery_error = latest_delivery_error
        # The log of the last failed delivery to Log Service.
        self.latest_delivery_log_service_error = latest_delivery_log_service_error
        # The most recent time when an event was delivered to Log Service.
        self.latest_delivery_log_service_time = latest_delivery_log_service_time
        # The most recent time when an event was delivered by the trail.
        self.latest_delivery_time = latest_delivery_time
        # Indicates whether the destination Object Storage Service (OSS) bucket is available. Valid values:
        # 
        # *   true
        # *   false
        self.oss_bucket_status = oss_bucket_status
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the destination Log Service Logstore is available. Valid values:
        # 
        # *   true
        # *   false
        self.sls_log_store_status = sls_log_store_status
        # The time when logging was last enabled for the trail.
        self.start_logging_time = start_logging_time
        # The time when logging was last disabled for the trail.
        self.stop_logging_time = stop_logging_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_logging is not None:
            result['IsLogging'] = self.is_logging
        if self.latest_delivery_error is not None:
            result['LatestDeliveryError'] = self.latest_delivery_error
        if self.latest_delivery_log_service_error is not None:
            result['LatestDeliveryLogServiceError'] = self.latest_delivery_log_service_error
        if self.latest_delivery_log_service_time is not None:
            result['LatestDeliveryLogServiceTime'] = self.latest_delivery_log_service_time
        if self.latest_delivery_time is not None:
            result['LatestDeliveryTime'] = self.latest_delivery_time
        if self.oss_bucket_status is not None:
            result['OssBucketStatus'] = self.oss_bucket_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_log_store_status is not None:
            result['SlsLogStoreStatus'] = self.sls_log_store_status
        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time
        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsLogging') is not None:
            self.is_logging = m.get('IsLogging')
        if m.get('LatestDeliveryError') is not None:
            self.latest_delivery_error = m.get('LatestDeliveryError')
        if m.get('LatestDeliveryLogServiceError') is not None:
            self.latest_delivery_log_service_error = m.get('LatestDeliveryLogServiceError')
        if m.get('LatestDeliveryLogServiceTime') is not None:
            self.latest_delivery_log_service_time = m.get('LatestDeliveryLogServiceTime')
        if m.get('LatestDeliveryTime') is not None:
            self.latest_delivery_time = m.get('LatestDeliveryTime')
        if m.get('OssBucketStatus') is not None:
            self.oss_bucket_status = m.get('OssBucketStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogStoreStatus') is not None:
            self.sls_log_store_status = m.get('SlsLogStoreStatus')
        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')
        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')
        return self


class GetTrailStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrailStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrailStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeliveryHistoryJobsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # *   Valid values: 1 to 100.
        # *   Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: str = None,
        home_region: str = None,
        job_id: int = None,
        job_status: int = None,
        start_time: str = None,
        trail_name: str = None,
        updated_time: str = None,
    ):
        # The time when the task was created.
        self.created_time = created_time
        # The time when the task ended.
        self.end_time = end_time
        # The home region of the trail.
        self.home_region = home_region
        # The task ID.
        self.job_id = job_id
        # The task status. Valid values:
        # 
        # *   0: The task is initializing.
        # *   1: The task is delivering historical events.
        # *   2: The task is complete.
        # *   3: The task fails.
        self.job_status = job_status
        # The time when the task started.
        self.start_time = start_time
        # The name of the trail.
        self.trail_name = trail_name
        # The time when the task was updated.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trail_name is not None:
            result['TrailName'] = self.trail_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListDeliveryHistoryJobsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_history_jobs: List[ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of historical event delivery tasks.
        self.delivery_history_jobs = delivery_history_jobs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of historical event delivery tasks returned.
        self.total_count = total_count

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
        result['DeliveryHistoryJobs'] = []
        if self.delivery_history_jobs is not None:
            for k in self.delivery_history_jobs:
                result['DeliveryHistoryJobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_history_jobs = []
        if m.get('DeliveryHistoryJobs') is not None:
            for k in m.get('DeliveryHistoryJobs'):
                temp_model = ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs()
                self.delivery_history_jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeliveryHistoryJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeliveryHistoryJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The key of the query condition. Valid values:
        # 
        # *  ServiceName: the name of a specific Alibaba Cloud service.
        # *  EventName: the name of a specific event.
        # *  User: the name of the RAM user who calls a specific operation.
        # *  EventId: the ID of a specific event.
        # *  ResourceType: the type of resources.
        # *   ResourceName: the name of a specific resource.
        # *   EventRW: the read/write type of events.
        # *  EventAccessKeyId: the AccessKey ID used in events.
        # 
        # > You can use only one query condition for each query.
        self.key = key
        # The value of the query condition. Valid values:
        # 
        # *   When the LookupAttribute.N.Key parameter is set to ServiceName, you can set this parameter to a value such as `Ecs`.
        # *   When the LookupAttribute.N.Key parameter is set to EventName, you can set this parameter to a value such as `ConsoleSignin`.
        # *   When the LookupAttribute.N.Key parameter is set to User, you can set this parameter to a value such as `Alice`.
        # *   When the LookupAttribute.N.Key parameter is set to EventId, you can set this parameter to a value such as `B702AFA3-FD4B-40E3-88E4-C0752FAA****`.
        # *   When the LookupAttribute.N.Key parameter is set to ResourceType, you can set this parameter to a value such as `ACS::ECS::Instance`.
        # *   When the LookupAttribute.N.Key parameter is set to ResourceName, you can set this parameter to a value such as `i-bp14664y88udkt45****`.
        # *   When the LookupAttribute.N.Key parameter is set to EventRW, you can set this parameter to `Read` or `Write`.
        # *   When the LookupAttribute.N.Key parameter is set to EventAccessKeyId, you can set this parameter to a value such as `LTAI4FoDkCf4DU1bic1V****`.
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
        direction: str = None,
        end_time: str = None,
        lookup_attribute: List[LookupEventsRequestLookupAttribute] = None,
        max_results: str = None,
        next_token: str = None,
        start_time: str = None,
    ):
        # The order in which details of events are to be retrieved. Valid values:
        # 
        # *   FORWARD: ascending order.
        # *   BACKWARD: descending order. This is the default value.
        self.direction = direction
        # The end of the time range to query. The default time is the current time. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        self.end_time = end_time
        # Query conditions.
        self.lookup_attribute = lookup_attribute
        # The maximum number of entries to be returned.
        # 
        # Valid values: 0 to 50.
        self.max_results = max_results
        # The token used to request the next page of query results.
        # 
        # > The request parameters must be the same as those of the last request.
        self.next_token = next_token
        # The beginning of the time range to query. The default time is seven days prior to the current time. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        self.start_time = start_time

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
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['LookupAttribute'] = []
        if self.lookup_attribute is not None:
            for k in self.lookup_attribute:
                result['LookupAttribute'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.lookup_attribute = []
        if m.get('LookupAttribute') is not None:
            for k in m.get('LookupAttribute'):
                temp_model = LookupEventsRequestLookupAttribute()
                self.lookup_attribute.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class LookupEventsResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        events: List[Dict[str, Any]] = None,
        next_token: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range when event details were queried.
        self.end_time = end_time
        # The returned event details.
        # 
        # For more information about the fields in an event log, see [ActionTrail event log reference](~~28819~~).
        self.events = events
        # The token used to return the next page of query results.
        # 
        # > This parameter is not returned if no more results are to be returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range when event details were queried.
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
        if self.events is not None:
            result['Events'] = self.events
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class LookupEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LookupEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LookupEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartLoggingRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the trail that you want to enable.
        # 
        # The name must be 6 to 36 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (\_). It must start with a lowercase letter.
        # 
        # > The name must be unique within your Alibaba Cloud account.
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
        # The ID of the request.
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
        status_code: int = None,
        body: StartLoggingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLoggingRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the trail that you want to disable.
        # 
        # The name must be 6 to 36 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (\_). It must start with a lowercase letter.
        # 
        # > The name must be unique within your Alibaba Cloud account.
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
        # The ID of the request.
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
        status_code: int = None,
        body: StopLoggingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGlobalEventsStorageRegionRequest(TeaModel):
    def __init__(
        self,
        storage_region: str = None,
    ):
        # The region where you want to store global events.
        # 
        # Valid values:
        # 
        # *   ap-southeast-1
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     the Singapore region
        # 
        #     <!-- -->
        # 
        # *   cn-hangzhou
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     the China (Hangzhou) region
        # 
        #     <!-- -->
        self.storage_region = storage_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')
        return self


class UpdateGlobalEventsStorageRegionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class UpdateGlobalEventsStorageRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGlobalEventsStorageRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGlobalEventsStorageRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrailRequest(TeaModel):
    def __init__(
        self,
        event_rw: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
    ):
        # The read/write type of the events to be delivered. Valid values:
        # 
        # *   Write: write events. It is the default value.
        # *   Read: read events.
        # *   All: read and write events.
        self.event_rw = event_rw
        # The name of the trail whose configurations you want to update.
        # 
        # The name must be 6 to 36 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores (\_). It must start with a lowercase letter.
        # 
        # >  The name must be unique within an Alibaba Cloud account.
        self.name = name
        # The name of the Object Storage Service (OSS) bucket to which you want to deliver events.
        # 
        # The name must be 3 to 63 characters in length. The name must start with a lowercase letter or a digit and can contain lowercase letters, digits, and hyphens (-).
        # 
        # >  Make sure that the bucket exists before you update the configuration of the trail.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the files that are stored in the OSS bucket.
        # 
        # The prefix must be 6 to 32 characters in length. The prefix must start with a letter and can contain letters, digits, hyphens (-), forward slashes (/), and underscores (\_).
        self.oss_key_prefix = oss_key_prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        # 
        # *   If you do not specify this parameter, ActionTrail creates a service-linked role to create the required resources. For more information, see [Manage the service-linked role](~~169244~~).
        # *   If you specify this parameter, you must grant the permissions of the service-linked role that is assumed by ActionTrail to the RAM role before you can deliver events to your Alibaba Cloud account. If you need to deliver events to other Alibaba Cloud accounts, you must attach the permission policy that is used to grant permissions related to event delivery to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](~~207462~~).
        self.oss_write_role_arn = oss_write_role_arn
        # The ARN of the Log Service project to which you want to deliver events.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the Log Service project.
        # 
        # *   If you do not specify this parameter, ActionTrail creates a service-linked role to create the corresponding resource. For more information, see [Manage the service-linked role](~~169244~~).
        # *   If you specify this parameter, you must grant the permissions of the service-linked role that is assumed by ActionTrail to the RAM role before you can deliver events to your Alibaba Cloud account. If you need to deliver events to other Alibaba Cloud accounts, you must attach the permission policy that is used to grant permissions related to event delivery to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](~~207462~~).
        self.sls_write_role_arn = sls_write_role_arn
        # The region of the trail.
        # 
        # *   The default value is All, which indicates that the trail delivers events from all regions.
        # 
        # You can also specify specific regions. You can call the [DescribeRegions](~~213597~~) operation to query all the supported regions.
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
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
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
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
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        return self


class UpdateTrailResponseBody(TeaModel):
    def __init__(
        self,
        event_rw: str = None,
        home_region: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        request_id: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
    ):
        # The read/write type of the events to be delivered.
        self.event_rw = event_rw
        # The home region of the trail.
        self.home_region = home_region
        # The name of the trail.
        self.name = name
        # The name of the OSS bucket.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the log files to be stored in the destination OSS bucket.
        self.oss_key_prefix = oss_key_prefix
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        self.oss_write_role_arn = oss_write_role_arn
        # The ID of the request.
        self.request_id = request_id
        # The ARN of the Log Service project to which events are to be delivered.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail is to deliver events to the Log Service project.
        self.sls_write_role_arn = sls_write_role_arn
        # The one or more regions from which the trail delivers events.
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.home_region is not None:
            result['HomeRegion'] = self.home_region
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn
        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn
        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')
        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')
        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')
        return self


class UpdateTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


