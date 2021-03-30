# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alinlp20200629 import models as alinlp_20200629_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('alinlp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_check_duplication_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetCheckDuplicationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCheckDuplicationChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_check_duplication_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetCheckDuplicationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCheckDuplicationChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_check_duplication_ch_medical(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_check_duplication_ch_medical_with_options(request, runtime)

    async def get_check_duplication_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_check_duplication_ch_medical_with_options_async(request, runtime)

    def get_diagnosis_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDiagnosisChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDiagnosisChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDiagnosisChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDiagnosisChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis_ch_medical(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_ch_medical_with_options(request, runtime)

    async def get_diagnosis_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_diagnosis_ch_medical_with_options_async(request, runtime)

    def get_dp_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDpChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dp_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDpChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dp_ch_ecom(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_ecom_with_options(request, runtime)

    async def get_dp_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_ecom_with_options_async(request, runtime)

    def get_dp_ch_general_ctbwith_options(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralCTB',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralCTBResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dp_ch_general_ctbwith_options_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralCTB',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralCTBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dp_ch_general_ctb(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_ctbwith_options(request, runtime)

    async def get_dp_ch_general_ctb_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_general_ctbwith_options_async(request, runtime)

    def get_dp_ch_general_stanford_with_options(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralStanford',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralStanfordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dp_ch_general_stanford_with_options_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralStanford',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralStanfordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dp_ch_general_stanford(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_stanford_with_options(request, runtime)

    async def get_dp_ch_general_stanford_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_general_stanford_with_options_async(request, runtime)

    def get_ec_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ec_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ec_ch_general(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ec_ch_general_with_options(request, runtime)

    async def get_ec_ch_general_async(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ec_ch_general_with_options_async(request, runtime)

    def get_ec_en_general_with_options(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEcEnGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcEnGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ec_en_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEcEnGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcEnGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ec_en_general(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ec_en_general_with_options(request, runtime)

    async def get_ec_en_general_async(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ec_en_general_with_options_async(request, runtime)

    def get_keyword_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetKeywordChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetKeywordChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_ch_ecom(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_ch_ecom_with_options(request, runtime)

    async def get_keyword_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_ch_ecom_with_options_async(request, runtime)

    def get_keyword_en_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetKeywordEnEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordEnEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_en_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetKeywordEnEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordEnEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_en_ecom(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_en_ecom_with_options(request, runtime)

    async def get_keyword_en_ecom_async(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_en_ecom_with_options_async(request, runtime)

    def get_medicine_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMedicineChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetMedicineChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_medicine_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMedicineChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetMedicineChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_medicine_ch_medical(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_medicine_ch_medical_with_options(request, runtime)

    async def get_medicine_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_medicine_ch_medical_with_options_async(request, runtime)

    def get_ner_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_ch_ecom(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_ecom_with_options(request, runtime)

    async def get_ner_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_ch_ecom_with_options_async(request, runtime)

    def get_ner_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_ch_medical(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_medical_with_options(request, runtime)

    async def get_ner_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_ch_medical_with_options_async(request, runtime)

    def get_ner_customized_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_customized_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_customized_ch_ecom(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_ch_ecom_with_options(request, runtime)

    async def get_ner_customized_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_customized_ch_ecom_with_options_async(request, runtime)

    def get_ner_customized_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_customized_sea_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedSeaEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_customized_sea_ecom(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_sea_ecom_with_options(request, runtime)

    async def get_ner_customized_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_customized_sea_ecom_with_options_async(request, runtime)

    def get_operation_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOperationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOperationChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOperationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOperationChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation_ch_medical(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_operation_ch_medical_with_options(request, runtime)

    async def get_operation_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_ch_medical_with_options_async(request, runtime)

    def get_pos_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPosChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pos_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPosChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pos_ch_ecom(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_ecom_with_options(request, runtime)

    async def get_pos_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pos_ch_ecom_with_options_async(request, runtime)

    def get_pos_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPosChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pos_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPosChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pos_ch_general(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_general_with_options(request, runtime)

    async def get_pos_ch_general_async(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pos_ch_general_with_options_async(request, runtime)

    def get_sa_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSaChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sa_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSaChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sa_ch_general(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sa_ch_general_with_options(request, runtime)

    async def get_sa_ch_general_async(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_ch_general_with_options_async(request, runtime)

    def get_sa_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSaSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sa_sea_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSaSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaSeaEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sa_sea_ecom(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sa_sea_ecom_with_options(request, runtime)

    async def get_sa_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_sea_ecom_with_options_async(request, runtime)

    def get_similarity_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSimilarityChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSimilarityChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_similarity_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSimilarityChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSimilarityChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_similarity_ch_medical(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_similarity_ch_medical_with_options(request, runtime)

    async def get_similarity_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_similarity_ch_medical_with_options_async(request, runtime)

    def get_summary_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSummaryChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSummaryChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSummaryChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSummaryChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_ch_ecom(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_summary_ch_ecom_with_options(request, runtime)

    async def get_summary_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_summary_ch_ecom_with_options_async(request, runtime)

    def get_tc_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTcChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tc_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTcChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tc_ch_ecom(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_ecom_with_options(request, runtime)

    async def get_tc_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tc_ch_ecom_with_options_async(request, runtime)

    def get_tc_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tc_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tc_ch_general(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_general_with_options(request, runtime)

    async def get_tc_ch_general_async(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tc_ch_general_with_options_async(request, runtime)

    def get_ts_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTsChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTsChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ts_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTsChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTsChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ts_ch_ecom(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ts_ch_ecom_with_options(request, runtime)

    async def get_ts_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ts_ch_ecom_with_options_async(request, runtime)

    def get_we_ch_comment_with_options(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_comment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_comment(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_comment_with_options(request, runtime)

    async def get_we_ch_comment_async(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_comment_with_options_async(request, runtime)

    def get_we_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_ecom(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_ecom_with_options(request, runtime)

    async def get_we_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_ecom_with_options_async(request, runtime)

    def get_we_ch_entertainment_with_options(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEntertainmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_entertainment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEntertainmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_entertainment(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_entertainment_with_options(request, runtime)

    async def get_we_ch_entertainment_async(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_entertainment_with_options_async(request, runtime)

    def get_we_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_general(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_general_with_options(request, runtime)

    async def get_we_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_general_with_options_async(request, runtime)

    def get_we_ch_search_with_options(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChSearch',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_search_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWeChSearch',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_search(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_search_with_options(request, runtime)

    async def get_we_ch_search_async(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_search_with_options_async(request, runtime)

    def get_ws_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_ch_general(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_ch_general_with_options(request, runtime)

    async def get_ws_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_ch_general_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_comment_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_ecom_comment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_comment(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_comment_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_comment_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_comment_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_content_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomContent',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_ecom_content_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomContent',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_content(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_content_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_content_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_content_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_title_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomTitle',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_ecom_title_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomTitle',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_title(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_title_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_title_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_title_with_options_async(request, runtime)

    def get_ws_customized_ch_entertainment_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_entertainment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_entertainment(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_entertainment_with_options(request, runtime)

    async def get_ws_customized_ch_entertainment_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_entertainment_with_options_async(request, runtime)

    def get_ws_customized_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_general(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_general_with_options(request, runtime)

    async def get_ws_customized_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_general_with_options_async(request, runtime)

    def get_ws_customized_ch_o2owith_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChO2O',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChO2OResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_o2owith_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChO2O',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChO2OResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_o2o(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_o2owith_options(request, runtime)

    async def get_ws_customized_ch_o2o_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_o2owith_options_async(request, runtime)

    def get_ws_customized_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_sea_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_sea_ecom(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_ecom_with_options(request, runtime)

    async def get_ws_customized_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_sea_ecom_with_options_async(request, runtime)

    def get_ws_customized_sea_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_sea_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_sea_general(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_general_with_options(request, runtime)

    async def get_ws_customized_sea_general_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_sea_general_with_options_async(request, runtime)

    def open_alinlp_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenAlinlpService',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.OpenAlinlpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_alinlp_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenAlinlpService',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.OpenAlinlpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_alinlp_service(self) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_alinlp_service_with_options(runtime)

    async def open_alinlp_service_async(self) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_alinlp_service_with_options_async(runtime)
