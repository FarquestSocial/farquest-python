# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from farquest import Farquest, AsyncFarquest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Farquest) -> None:
        organization = client.organizations.create(
            auth_redirect_url="string",
            callback_url="string",
            name="string",
        )
        assert organization is None

    @parametrize
    def test_raw_response_create(self, client: Farquest) -> None:
        response = client.organizations.with_raw_response.create(
            auth_redirect_url="string",
            callback_url="string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @parametrize
    def test_streaming_response_create(self, client: Farquest) -> None:
        with client.organizations.with_streaming_response.create(
            auth_redirect_url="string",
            callback_url="string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFarquest) -> None:
        organization = await async_client.organizations.create(
            auth_redirect_url="string",
            callback_url="string",
            name="string",
        )
        assert organization is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFarquest) -> None:
        response = await async_client.organizations.with_raw_response.create(
            auth_redirect_url="string",
            callback_url="string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFarquest) -> None:
        async with async_client.organizations.with_streaming_response.create(
            auth_redirect_url="string",
            callback_url="string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True
