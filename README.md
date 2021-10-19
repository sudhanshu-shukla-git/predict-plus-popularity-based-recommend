# predict-plus
## APIs

### Performance Based

#### https://predict-plus-recommender.herokuapp.com/performance_based

#### Sample Request : https://predict-plus-recommender.herokuapp.com/performance_based?mf_category=Debt%20Scheme&mf_sub_category=Liquid&risk=Moderate&top_n=5&load_cache=False
#### Method: GET
#### Allowed Values : 
#### Sample Result: 

```json
[{"1-Year Return(%)- Direct":"3.28","1-Year Return(%)- Regular":"3.21","3-Year Return(%)- Direct":"5.10","3-Year Return(%)- Regular":"5.04","5-Year Return(%)- Direct":"5.88","5-Year Return(%)- Regular":"5.81","benchmark":"NIFTY Liquid Fund Index","latest NAV- Direct":"2,325.0887","latest NAV- Regular":"2,311.9423","risk":"Moderate","scheme_name":"Axis Liquid Fund"},{"1-Year Return(%)- Direct":"3.25","1-Year Return(%)- Regular":"3.17","3-Year Return(%)- Direct":"4.98","3-Year Return(%)- Regular":"4.89","5-Year Return(%)- Direct":"5.80","5-Year Return(%)- Regular":"5.71","benchmark":"CRISIL Liquid Fund Index","latest NAV- Direct":"2,408.2207","latest NAV- Regular":"2,388.7586","risk":"Moderate","scheme_name":"BOI AXA Liquid Fund"},{"1-Year Return(%)- Direct":"3.42","1-Year Return(%)- Regular":"3.17","3-Year Return(%)- Direct":"5.19","3-Year Return(%)- Regular":"4.96","5-Year Return(%)- Direct":"5.89","5-Year Return(%)- Regular":"5.70","benchmark":"NIFTY Liquid Fund Index","latest NAV- Direct":"2,702.5092","latest NAV- Regular":"2,668.2378","risk":"Moderate","scheme_name":"Edelweiss Liquid Fund"},{"1-Year Return(%)- Direct":"3.23","1-Year Return(%)- Regular":"3.13","3-Year Return(%)- Direct":"5.01","3-Year Return(%)- Regular":"4.91","5-Year Return(%)- Direct":"5.76","5-Year Return(%)- Regular":"5.65","benchmark":"CRISIL Liquid Fund Index","latest NAV- Direct":"4,116.2249","latest NAV- Regular":"4,085.7339","risk":"Moderate","scheme_name":"HDFC Liquid Fund"},{"1-Year Return(%)- Direct":"2.93","1-Year Return(%)- Regular":"2.88","3-Year Return(%)- Direct":"4.41","3-Year Return(%)- Regular":"4.36","5-Year Return(%)- Direct":"5.25","5-Year Return(%)- Regular":"5.20","benchmark":"CRISIL Liquid Fund Index","latest NAV- Direct":"1,615.7312","latest NAV- Regular":"1,609.3442","risk":"Moderate","scheme_name":"IIFL Liquid Fund"}]
```
