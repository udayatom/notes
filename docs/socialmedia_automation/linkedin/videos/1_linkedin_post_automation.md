<iframe
  width="500" 
  height="500" 
  src="https://www.youtube.com/watch?v=xIsCBTZ7M_A"
  frameborder="0"
  allowfullscreen>
</iframe>


URL1: This is url asks the authentication, showing success message, That updated url is URL2

https://linkedin.com/oauth/v2/authorization?response_type=code&client_id=77fiy7xx2fq77x&redirect_uri=https://oauth.pstmn.io/v1/callback&state=bsdk&scope=openid%20profile%20email%20w_member_social

URL2:

https://oauth.pstmn.io/v1/callback?code=AQTYtAnnrept7eAoZvushFQTwStEb9oR0e8z0MkuNAou1RhjNFcX8OBrLzA0lsA4z1KdZmCFvCjxlJujffZfyvNMXogmaCzD_StGk7wj7w7SVhM_LaLrGzApHC2j9R3Xn_J_UQsPZkQuy5TCo8xe_9ZUQnV7Sg2sETczNA6Ym_2UF28epoPz9e3K7ZKXSxg3G74OP-vH8sb3xIPjXfk&state=bsdk

- In the URL2, code querystring value need to extract, This is the temporary token need to make the post call.

https://www.linkedin.com/oauth/v2/accesstoken - post request
x-www-form-urlencoded
params

- code : AQTYtAnnrept7eAoZvushFQTwStEb9oR0e8z0MkuNAou1RhjNFcX8OBrLzA0lsA4z1KdZmCFvCjxlJujffZfyvNMXogmaCzD_StGk7wj7w7SVhM_LaLrGzApHC2j9R3Xn_J_UQsPZkQuy5TCo8xe_9ZUQnV7Sg2sETczNA6Ym_2UF28epoPz9e3K7ZKXSxg3G74OP-vH8sb3xIPjXfk

- redirecturl :https://oauth.pstmn.io/v1/callback
- client_id:  need to taken from linkedin app console
- client_secret: need to taken from linkedin app console
- grant_type: authroization_code

In the final result, we can get the access_token, this token helps for use the linkedin api.
