# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eduembed20240101 import models as edu_embed_20240101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eduembed', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_lab_reservation_with_options(
        self,
        request: edu_embed_20240101_models.CreateLabReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.CreateLabReservationResponse:
        """
        @summary 创建实验预约
        
        @param request: CreateLabReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabReservationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lab_id):
            body['LabId'] = request.lab_id
        if not UtilClient.is_unset(request.member_count):
            body['MemberCount'] = request.member_count
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabReservation',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.CreateLabReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lab_reservation_with_options_async(
        self,
        request: edu_embed_20240101_models.CreateLabReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.CreateLabReservationResponse:
        """
        @summary 创建实验预约
        
        @param request: CreateLabReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabReservationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lab_id):
            body['LabId'] = request.lab_id
        if not UtilClient.is_unset(request.member_count):
            body['MemberCount'] = request.member_count
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabReservation',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.CreateLabReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lab_reservation(
        self,
        request: edu_embed_20240101_models.CreateLabReservationRequest,
    ) -> edu_embed_20240101_models.CreateLabReservationResponse:
        """
        @summary 创建实验预约
        
        @param request: CreateLabReservationRequest
        @return: CreateLabReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lab_reservation_with_options(request, runtime)

    async def create_lab_reservation_async(
        self,
        request: edu_embed_20240101_models.CreateLabReservationRequest,
    ) -> edu_embed_20240101_models.CreateLabReservationResponse:
        """
        @summary 创建实验预约
        
        @param request: CreateLabReservationRequest
        @return: CreateLabReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lab_reservation_with_options_async(request, runtime)

    def create_lab_session_with_options(
        self,
        request: edu_embed_20240101_models.CreateLabSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.CreateLabSessionResponse:
        """
        @summary 创建实验会话
        
        @param request: CreateLabSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.lab_id):
            body['LabId'] = request.lab_id
        if not UtilClient.is_unset(request.ram_account_id):
            body['RamAccountId'] = request.ram_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabSession',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.CreateLabSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lab_session_with_options_async(
        self,
        request: edu_embed_20240101_models.CreateLabSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.CreateLabSessionResponse:
        """
        @summary 创建实验会话
        
        @param request: CreateLabSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.lab_id):
            body['LabId'] = request.lab_id
        if not UtilClient.is_unset(request.ram_account_id):
            body['RamAccountId'] = request.ram_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabSession',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.CreateLabSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lab_session(
        self,
        request: edu_embed_20240101_models.CreateLabSessionRequest,
    ) -> edu_embed_20240101_models.CreateLabSessionResponse:
        """
        @summary 创建实验会话
        
        @param request: CreateLabSessionRequest
        @return: CreateLabSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lab_session_with_options(request, runtime)

    async def create_lab_session_async(
        self,
        request: edu_embed_20240101_models.CreateLabSessionRequest,
    ) -> edu_embed_20240101_models.CreateLabSessionResponse:
        """
        @summary 创建实验会话
        
        @param request: CreateLabSessionRequest
        @return: CreateLabSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lab_session_with_options_async(request, runtime)

    def describe_course_with_options(
        self,
        request: edu_embed_20240101_models.DescribeCourseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeCourseResponse:
        """
        @summary 查看课程详情
        
        @param request: DescribeCourseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCourseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_id):
            query['CourseId'] = request.course_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCourse',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeCourseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_course_with_options_async(
        self,
        request: edu_embed_20240101_models.DescribeCourseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeCourseResponse:
        """
        @summary 查看课程详情
        
        @param request: DescribeCourseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCourseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_id):
            query['CourseId'] = request.course_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCourse',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeCourseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_course(
        self,
        request: edu_embed_20240101_models.DescribeCourseRequest,
    ) -> edu_embed_20240101_models.DescribeCourseResponse:
        """
        @summary 查看课程详情
        
        @param request: DescribeCourseRequest
        @return: DescribeCourseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_course_with_options(request, runtime)

    async def describe_course_async(
        self,
        request: edu_embed_20240101_models.DescribeCourseRequest,
    ) -> edu_embed_20240101_models.DescribeCourseResponse:
        """
        @summary 查看课程详情
        
        @param request: DescribeCourseRequest
        @return: DescribeCourseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_course_with_options_async(request, runtime)

    def describe_course_lesson_with_options(
        self,
        request: edu_embed_20240101_models.DescribeCourseLessonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeCourseLessonResponse:
        """
        @summary 查看课程课时详情
        
        @param request: DescribeCourseLessonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCourseLessonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lesson_id):
            query['LessonId'] = request.lesson_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCourseLesson',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeCourseLessonResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_course_lesson_with_options_async(
        self,
        request: edu_embed_20240101_models.DescribeCourseLessonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeCourseLessonResponse:
        """
        @summary 查看课程课时详情
        
        @param request: DescribeCourseLessonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCourseLessonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lesson_id):
            query['LessonId'] = request.lesson_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCourseLesson',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeCourseLessonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_course_lesson(
        self,
        request: edu_embed_20240101_models.DescribeCourseLessonRequest,
    ) -> edu_embed_20240101_models.DescribeCourseLessonResponse:
        """
        @summary 查看课程课时详情
        
        @param request: DescribeCourseLessonRequest
        @return: DescribeCourseLessonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_course_lesson_with_options(request, runtime)

    async def describe_course_lesson_async(
        self,
        request: edu_embed_20240101_models.DescribeCourseLessonRequest,
    ) -> edu_embed_20240101_models.DescribeCourseLessonResponse:
        """
        @summary 查看课程课时详情
        
        @param request: DescribeCourseLessonRequest
        @return: DescribeCourseLessonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_course_lesson_with_options_async(request, runtime)

    def describe_lab_with_options(
        self,
        request: edu_embed_20240101_models.DescribeLabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeLabResponse:
        """
        @summary 查看实验详情
        
        @param request: DescribeLabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLabResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLab',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeLabResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lab_with_options_async(
        self,
        request: edu_embed_20240101_models.DescribeLabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeLabResponse:
        """
        @summary 查看实验详情
        
        @param request: DescribeLabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLabResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLab',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeLabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lab(
        self,
        request: edu_embed_20240101_models.DescribeLabRequest,
    ) -> edu_embed_20240101_models.DescribeLabResponse:
        """
        @summary 查看实验详情
        
        @param request: DescribeLabRequest
        @return: DescribeLabResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lab_with_options(request, runtime)

    async def describe_lab_async(
        self,
        request: edu_embed_20240101_models.DescribeLabRequest,
    ) -> edu_embed_20240101_models.DescribeLabResponse:
        """
        @summary 查看实验详情
        
        @param request: DescribeLabRequest
        @return: DescribeLabResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lab_with_options_async(request, runtime)

    def describe_lab_reservation_with_options(
        self,
        request: edu_embed_20240101_models.DescribeLabReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeLabReservationResponse:
        """
        @summary 查询实验预约
        
        @param request: DescribeLabReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLabReservationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLabReservation',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeLabReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lab_reservation_with_options_async(
        self,
        request: edu_embed_20240101_models.DescribeLabReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeLabReservationResponse:
        """
        @summary 查询实验预约
        
        @param request: DescribeLabReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLabReservationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLabReservation',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeLabReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lab_reservation(
        self,
        request: edu_embed_20240101_models.DescribeLabReservationRequest,
    ) -> edu_embed_20240101_models.DescribeLabReservationResponse:
        """
        @summary 查询实验预约
        
        @param request: DescribeLabReservationRequest
        @return: DescribeLabReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lab_reservation_with_options(request, runtime)

    async def describe_lab_reservation_async(
        self,
        request: edu_embed_20240101_models.DescribeLabReservationRequest,
    ) -> edu_embed_20240101_models.DescribeLabReservationResponse:
        """
        @summary 查询实验预约
        
        @param request: DescribeLabReservationRequest
        @return: DescribeLabReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lab_reservation_with_options_async(request, runtime)

    def describe_lab_session_with_options(
        self,
        request: edu_embed_20240101_models.DescribeLabSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeLabSessionResponse:
        """
        @summary 查看实验会话信息
        
        @param request: DescribeLabSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLabSessionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLabSession',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeLabSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lab_session_with_options_async(
        self,
        request: edu_embed_20240101_models.DescribeLabSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.DescribeLabSessionResponse:
        """
        @summary 查看实验会话信息
        
        @param request: DescribeLabSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLabSessionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLabSession',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.DescribeLabSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lab_session(
        self,
        request: edu_embed_20240101_models.DescribeLabSessionRequest,
    ) -> edu_embed_20240101_models.DescribeLabSessionResponse:
        """
        @summary 查看实验会话信息
        
        @param request: DescribeLabSessionRequest
        @return: DescribeLabSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lab_session_with_options(request, runtime)

    async def describe_lab_session_async(
        self,
        request: edu_embed_20240101_models.DescribeLabSessionRequest,
    ) -> edu_embed_20240101_models.DescribeLabSessionResponse:
        """
        @summary 查看实验会话信息
        
        @param request: DescribeLabSessionRequest
        @return: DescribeLabSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lab_session_with_options_async(request, runtime)

    def list_courses_with_options(
        self,
        request: edu_embed_20240101_models.ListCoursesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.ListCoursesResponse:
        """
        @summary 查看课程列表
        
        @param request: ListCoursesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCoursesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCourses',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.ListCoursesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_courses_with_options_async(
        self,
        request: edu_embed_20240101_models.ListCoursesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.ListCoursesResponse:
        """
        @summary 查看课程列表
        
        @param request: ListCoursesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCoursesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCourses',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.ListCoursesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_courses(
        self,
        request: edu_embed_20240101_models.ListCoursesRequest,
    ) -> edu_embed_20240101_models.ListCoursesResponse:
        """
        @summary 查看课程列表
        
        @param request: ListCoursesRequest
        @return: ListCoursesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_courses_with_options(request, runtime)

    async def list_courses_async(
        self,
        request: edu_embed_20240101_models.ListCoursesRequest,
    ) -> edu_embed_20240101_models.ListCoursesResponse:
        """
        @summary 查看课程列表
        
        @param request: ListCoursesRequest
        @return: ListCoursesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_courses_with_options_async(request, runtime)

    def page_list_lab_reservations_with_options(
        self,
        request: edu_embed_20240101_models.PageListLabReservationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.PageListLabReservationsResponse:
        """
        @summary 分页查询实验预约
        
        @param request: PageListLabReservationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListLabReservationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageListLabReservations',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.PageListLabReservationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_list_lab_reservations_with_options_async(
        self,
        request: edu_embed_20240101_models.PageListLabReservationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.PageListLabReservationsResponse:
        """
        @summary 分页查询实验预约
        
        @param request: PageListLabReservationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListLabReservationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageListLabReservations',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.PageListLabReservationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_list_lab_reservations(
        self,
        request: edu_embed_20240101_models.PageListLabReservationsRequest,
    ) -> edu_embed_20240101_models.PageListLabReservationsResponse:
        """
        @summary 分页查询实验预约
        
        @param request: PageListLabReservationsRequest
        @return: PageListLabReservationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.page_list_lab_reservations_with_options(request, runtime)

    async def page_list_lab_reservations_async(
        self,
        request: edu_embed_20240101_models.PageListLabReservationsRequest,
    ) -> edu_embed_20240101_models.PageListLabReservationsResponse:
        """
        @summary 分页查询实验预约
        
        @param request: PageListLabReservationsRequest
        @return: PageListLabReservationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.page_list_lab_reservations_with_options_async(request, runtime)

    def page_list_lab_sessions_with_options(
        self,
        request: edu_embed_20240101_models.PageListLabSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.PageListLabSessionsResponse:
        """
        @summary 分页查询实验会话
        
        @param request: PageListLabSessionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListLabSessionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageListLabSessions',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.PageListLabSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_list_lab_sessions_with_options_async(
        self,
        request: edu_embed_20240101_models.PageListLabSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.PageListLabSessionsResponse:
        """
        @summary 分页查询实验会话
        
        @param request: PageListLabSessionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListLabSessionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageListLabSessions',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.PageListLabSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_list_lab_sessions(
        self,
        request: edu_embed_20240101_models.PageListLabSessionsRequest,
    ) -> edu_embed_20240101_models.PageListLabSessionsResponse:
        """
        @summary 分页查询实验会话
        
        @param request: PageListLabSessionsRequest
        @return: PageListLabSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.page_list_lab_sessions_with_options(request, runtime)

    async def page_list_lab_sessions_async(
        self,
        request: edu_embed_20240101_models.PageListLabSessionsRequest,
    ) -> edu_embed_20240101_models.PageListLabSessionsResponse:
        """
        @summary 分页查询实验会话
        
        @param request: PageListLabSessionsRequest
        @return: PageListLabSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.page_list_lab_sessions_with_options_async(request, runtime)

    def page_list_labs_with_options(
        self,
        request: edu_embed_20240101_models.PageListLabsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.PageListLabsResponse:
        """
        @summary 分页查询实验
        
        @param request: PageListLabsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListLabsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageListLabs',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.PageListLabsResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_list_labs_with_options_async(
        self,
        request: edu_embed_20240101_models.PageListLabsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.PageListLabsResponse:
        """
        @summary 分页查询实验
        
        @param request: PageListLabsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListLabsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageListLabs',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.PageListLabsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_list_labs(
        self,
        request: edu_embed_20240101_models.PageListLabsRequest,
    ) -> edu_embed_20240101_models.PageListLabsResponse:
        """
        @summary 分页查询实验
        
        @param request: PageListLabsRequest
        @return: PageListLabsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.page_list_labs_with_options(request, runtime)

    async def page_list_labs_async(
        self,
        request: edu_embed_20240101_models.PageListLabsRequest,
    ) -> edu_embed_20240101_models.PageListLabsResponse:
        """
        @summary 分页查询实验
        
        @param request: PageListLabsRequest
        @return: PageListLabsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.page_list_labs_with_options_async(request, runtime)

    def remove_lab_reservation_with_options(
        self,
        request: edu_embed_20240101_models.RemoveLabReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.RemoveLabReservationResponse:
        """
        @summary 移除实验预约
        
        @param request: RemoveLabReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveLabReservationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.lab_reservation_id):
            body['LabReservationId'] = request.lab_reservation_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveLabReservation',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.RemoveLabReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_lab_reservation_with_options_async(
        self,
        request: edu_embed_20240101_models.RemoveLabReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_embed_20240101_models.RemoveLabReservationResponse:
        """
        @summary 移除实验预约
        
        @param request: RemoveLabReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveLabReservationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.lab_reservation_id):
            body['LabReservationId'] = request.lab_reservation_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveLabReservation',
            version='2024-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_embed_20240101_models.RemoveLabReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_lab_reservation(
        self,
        request: edu_embed_20240101_models.RemoveLabReservationRequest,
    ) -> edu_embed_20240101_models.RemoveLabReservationResponse:
        """
        @summary 移除实验预约
        
        @param request: RemoveLabReservationRequest
        @return: RemoveLabReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_lab_reservation_with_options(request, runtime)

    async def remove_lab_reservation_async(
        self,
        request: edu_embed_20240101_models.RemoveLabReservationRequest,
    ) -> edu_embed_20240101_models.RemoveLabReservationResponse:
        """
        @summary 移除实验预约
        
        @param request: RemoveLabReservationRequest
        @return: RemoveLabReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_lab_reservation_with_options_async(request, runtime)
