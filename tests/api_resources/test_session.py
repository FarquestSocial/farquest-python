# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from farquest import Farquest, AsyncFarquest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_correlated(self, client: Farquest) -> None:
        session = client.session.create_correlated(
            path_correlated_id="string",
            body_correlated_id="string",
        )
        assert session is None

    @parametrize
    def test_raw_response_create_correlated(self, client: Farquest) -> None:
        response = client.session.with_raw_response.create_correlated(
            path_correlated_id="string",
            body_correlated_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_create_correlated(self, client: Farquest) -> None:
        with client.session.with_streaming_response.create_correlated(
            path_correlated_id="string",
            body_correlated_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_correlated(self, client: Farquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_correlated_id` but received ''"):
            client.session.with_raw_response.create_correlated(
                path_correlated_id="",
                body_correlated_id="",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_correlated(self, async_client: AsyncFarquest) -> None:
        session = await async_client.session.create_correlated(
            path_correlated_id="string",
            body_correlated_id="string",
        )
        assert session is None

    @parametrize
    async def test_raw_response_create_correlated(self, async_client: AsyncFarquest) -> None:
        response = await async_client.session.with_raw_response.create_correlated(
            path_correlated_id="string",
            body_correlated_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_create_correlated(self, async_client: AsyncFarquest) -> None:
        async with async_client.session.with_streaming_response.create_correlated(
            path_correlated_id="string",
            body_correlated_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_correlated(self, async_client: AsyncFarquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_correlated_id` but received ''"):
            await async_client.session.with_raw_response.create_correlated(
                path_correlated_id="",
                body_correlated_id="",
            )
